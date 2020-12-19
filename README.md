<img src="docs/img/pybtc.png" width="100">

## Python bitgesell library

Based on pybtc library. Current version is 3.0


### Feature Support

* Basic functions
* Supports addresses types PUBKEY, P2PKH, P2SH, P2SH-PWPKH, P2WPKH, P2WSH.
* Supports BIP32(Hierarchical Deterministic Wallets), BIP39(Mnemonic code generation)
* Supports BIP141(Segregated Witness)
* Transaction constructor


### Installation

To install pybgl

    $ git clone https://github.com/bitaps-com/pybgl
    $ cd pybgl
    $ python3 setup.py install
    
### Dependencies

* Python 3.3.3+


### Documentation

Documentation is available at https://pybgl.readthedocs.io

### Example of usage

##### Create address

      >>> import pybgl
      >>> a = pybgl.Address()
      >>> a.address
      'bgl1qdzjn6rd7e84lt2m5d3yf9jcg42ncdje7vhp4rl'
      >>> a.private_key.wif
      'L1LAHLFBWcW2E1xRsUooVL9ajxJXtsAUjJJ4GuPTgHKAKNhy6fsD'
      >>> a = pybgl.Address('L1LAHLFBWcW2E1xRsUooVL9ajxJXtsAUjJJ4GuPTgHKAKNhy6fsD')
      >>> a.address
      'bgl1qdzjn6rd7e84lt2m5d3yf9jcg42ncdje7vhp4rl'

##### Create private key


      >>> import pybgl
      >>> pybgl.create_private_key()
      'L38PPqhzCbyTH3nd7e2ExEY3LSdaYhaF1d7pXYBEz83avPfpBbZ6'
      >>> pybgl.create_private_key(compressed=False)
      '5JCnJEggRKX5rscdGiqasmYdsyQ2fCYyLA7xYqSDRLEbWY7mZtq'


##### Create wallet

      >>> import pybgl
      >>> w = pybgl.Wallet(path_type='BIP84')
      >>> w.mnemonic
      'wet talent menu also ill comic smart unfold bone tape settle kangaroo caught tree wrap write diagram stomach have time addict unknown cruise polar'
      >>> w.account_public_xkey
      'zpub6qhAnVjudYd5rA4tCViT1iC5TQs9nPKhF2JcBZ55VnsN7EYGhnVr5X14enqueqWuz2nBBaDr77WT1Rnx82R1mTAbr9FbJq8oNdcf8UgndVA'
      >>> w = pybgl.Wallet('wet talent menu also ill comic smart unfold bone tape settle kangaroo caught tree wrap write diagram stomach have time addict unknown cruise polar',path_type='BIP84')
      >>> w.account_public_xkey
      'zpub6qhAnVjudYd5rA4tCViT1iC5TQs9nPKhF2JcBZ55VnsN7EYGhnVr5X14enqueqWuz2nBBaDr77WT1Rnx82R1mTAbr9FbJq8oNdcf8UgndVA'
      >>> w.get_address(0)['address']
      'bgl1qjc46yw4zgggj4e0x6ew6htuu234j4y9vds66e2'
      >>> w.get_address(0)['private_key']
      'L1U3Fviv4PGDxQatgXimWnU8yLy6jVz12wAyxjjP4XLyjDx7aycU'
      >>> w.get_address(0)['public_key']

### How to Contribute

In order to make a clone of the GitHub repo: open the link and press the “Fork” button on the upper-right menu of the web page.

Workflow is pretty straightforward:

1. Clone the GitHub
2. Make a change
3. Make sure all tests passed
4. Add a record into file into change.log.
5. Commit changes to own pybgl clone
6. Make pull request from github page for your clone against master branch


