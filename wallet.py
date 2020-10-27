import subprocess
import json
import os
from dotenv import load_dotenv
from constants import *
from web3 import Web3
from eth_account import Account
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

load_dotenv()

# Set mnemonic as an environmental variable

mnemonic = os.getenv('MNEMONIC', 'eyebrow fat relax into latin have permit fine bridge annual galaxy denial')
# print(mnemonic)

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

def derive_wallets(mnemonic, coin, numderive):
    # Function that uses subprocess library to call the ./derive script from Python
    # Mnemonic, coin, and numderive are flags that must be passed into the shell command as variables
    # Numderive is a variable that sets the number of child keys generated

    command = f'./derive -g --mnemonic="{mnemonic}" --coin="{coin}" --numderive="{numderive}" --cols=address,index,path,address,privkey,pubkey,pubkeyhash,xprv,xpub --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()

    # Parse output into a JSON object
    keys = json.loads(output)
    return (keys)

# Dictionary called coins that derives ETH and BTCTEST wallets

coins = {
    "btc-test" : derive_wallets(mnemonic, BTCTEST, 3),
    "eth": derive_wallets(mnemonic, ETH, 3) 
    }

# Function that will convert the privkey string in a child key to an account object that bit or web3.py can use to transact.

def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

# Function that will create the raw, unsigned transaction that contains all metadata needed to transact.

def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas({
            "from": account.address,
            "to": to,
            "value": amount
        })
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice":w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address)
        }
    
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

# This function will call the function create_tx, sign the transaction, then send it to the designated network.

def send_tx(coin, account, to, amount):

    raw_tx = create_tx(coin, account, to, amount)
    sign_raw_tx = account.sign_transaction(raw_tx)

    if coin == ETH:
        send_to_blockchain = w3.eth.sendRawTransaction(sign_raw_tx.rawTransaction)
        return send_to_blockchain
    elif coin == BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(sign_raw_tx)

# Sending ETH transaction
eth_sender_account = priv_key_to_account(ETH,coins["eth"][0]['privkey'])
eth_recipient_address = coins["eth"][1]["address"]

send_tx(ETH, eth_sender_account, eth_recipient_address, 2)

# Bitcoin Testnet transaction
btctest_sender_account = priv_key_to_account(BTCTEST,coins["btc-test"][0]['privkey'])
btctest_recipient_address = coins["btc-test"][1]["address"]

send_tx(BTCTEST, btctest_sender_account, btctest_recipient_address, .0001)
