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

