# Multi_Blockchain_Wallet_in_Python

The goal of this project was to create a multi-blockchain wallet in python that can hold multiple crypto-assets. 
This particular wallet holds 2 coins:
* Ethereum
* Bitcoin Testnet

The wallet uses a command line tool, hd-wallet-derive, that supports not only BIP32, BIP39, and BIP44, but also supports non-standard derivation paths for the most popular wallets out there today!

## Dependencies

* PHP must be installed on your operating system
* You will need to clone the hd-wallet-derive tool.
* bit Python Bitcoin library.
* web3.py Python Ethereum library.

## Installing and Running hd-wallet-derive

1. Create a project directory called wallet and cd into it.
2. Clone the hd-wallet-derive tool into this folder and install it using the instructions on its `README.md`.
    - `git clone https://github.com/dan-da/hd-wallet-derive`
    - `cd hd-wallet-derive`
    - `php -r "readfile('https://getcomposer.org/installer');" | php`
    - `php composer.phar install`
3. Create a symlink called derive for the `hd-wallet-derive/hd-wallet-derive.php` script into the top level project directory like so: `ln -s hd-wallet-derive/hd-wallet-derive.php derive`
  - This will clean up the command needed to run the script in our code, as we can call `./derive` instead of `./hd-wallet-derive/hd-wallet-derive.php`.
4. Test that you can run the `./derive` script properly, use one of the examples on the repo's `README.md`

## Test Transactions:

### Bitcoin Testnet Transaction

1. Funded a BTCTEST address using a testnet faucet.
2. Used a block explorer to watch transactions on the address.
3. Sent a transaction to another testnet address.
    - Used the following snippet of code to send the transaction (rest of code can be found in wallet.py):
        - `btctest_sender_account = priv_key_to_account(BTCTEST,coins["btc-test"][0]['privkey'])`
        - `btctest_recipient_address = coins["btc-test"][1]["address"]`
        - `send_tx(BTCTEST, btctest_sender_account, btctest_recipient_address, .0001)`
        
![image](https://user-images.githubusercontent.com/65314799/97379063-e23e7280-1891-11eb-9d55-bdd025245bf3.png)

### Ethereum Transaction

* Due to a bug in web3.py, I sent a transaction or two with MyCrypto first, since the w3.eth.generateGasPrice() function does not work with an empty chain. 
* Sent a transaction from a pre-funded address in ganache to another, then copied the txid into MyCrypto's TX Status

**Screenshot of MyCrypto transaction:**

![image](https://user-images.githubusercontent.com/65314799/97379728-69401a80-1893-11eb-8114-4ec4e4740f3e.png)

* Sent another transaction with the following snippet of code:
    - `eth_sender_account = priv_key_to_account(ETH,coins["eth"][0]['privkey'])`
    - `eth_recipient_address = coins["eth"][1]["address"]`
    - `send_tx(ETH, eth_sender_account, eth_recipient_address, 2)`
    
**Screenshot of the test transaction from ganache:**

![image](https://user-images.githubusercontent.com/65314799/97379743-765d0980-1893-11eb-94d1-0bcba8065f23.png)
