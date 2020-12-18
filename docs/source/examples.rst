========
Examples
========


Create address
--------------

This is example of usage Address class. The address class implements the work with addresses controlled by a private key.
Supports the ability to create P2WPKH, P2PKH, PUBKEY address types and P2SH_P2WPKH as exception for SEGWIT adoption.
It is recommended to use native SEGWIT address type - P2WPKH, which reduces costs of miner fee and expand block capacity.
To create an address, you need to create a class object. Buy default,
will be created P2WPKH address for mainnet.



.. code-block:: bash

      >>> import pybgl
      >>> a = pybgl.Address()
      >>> a.address
      'bgl1qdzjn6rd7e84lt2m5d3yf9jcg42ncdje7vhp4rl'
      >>> a.private_key.wif
      'L1LAHLFBWcW2E1xRsUooVL9ajxJXtsAUjJJ4GuPTgHKAKNhy6fsD'
      >>>



Get address from key
--------------------

In case you already have private or public key you can object from your key.

.. code-block:: bash

      >>> a = pybgl.Address('L1LAHLFBWcW2E1xRsUooVL9ajxJXtsAUjJJ4GuPTgHKAKNhy6fsD')
      >>> a.address
      'bgl1qdzjn6rd7e84lt2m5d3yf9jcg42ncdje7vhp4rl'
      >>> a.public_key.hex
      '028608fe359c6ffa37f2429279145e627feff745b2e35fe1f4fcabc1759005ddc7'
      >>>
      >>> # get address from public key
      >>> pub = pybgl.PublicKey('028608fe359c6ffa37f2429279145e627feff745b2e35fe1f4fcabc1759005ddc7')
      >>>
      >>> pybgl.Address(pub).address
      'bgl1qdzjn6rd7e84lt2m5d3yf9jcg42ncdje7vhp4rl'
      >>>

Pure functions for address
--------------------------

Create private key

.. code-block:: bash

      >>> import pybgl
      >>> pybgl.create_private_key()
      'L38PPqhzCbyTH3nd7e2ExEY3LSdaYhaF1d7pXYBEz83avPfpBbZ6'
      >>>
      >>> pybgl.create_private_key(compressed=False)
      '5JCnJEggRKX5rscdGiqasmYdsyQ2fCYyLA7xYqSDRLEbWY7mZtq'
      >>>
      >>> pybgl.is_wif_valid('5JCnJEggRKX5rscdGiqasmYdsyQ2fCYyLA7xYqSDRLEbWY7mZtq')
      True
      >>> pybgl.is_wif_valid('5JCnJEggRKX5rscdGiqasmYds*******yLA7xYqSDRLEbWY7mZtq')
      False
      >>>


Tools

.. code-block:: bash

      >>> pybgl.is_address_valid('bgl1qdzjn6rd7e84lt2m5d3yf9jcg42ncdje7vhp4rl')
      True
      >>> pybgl.address_type('bgl1qdzjn6rd7e84lt2m5d3yf9jcg42ncdje7vhp4rl')
      'P2WPKH'
      >>> pybgl.address_net_type('bgl1qdzjn6rd7e84lt2m5d3yf9jcg42ncdje7vhp4rl')
      'mainnet'
      >>>



Create wallet
--------------

This is example of usage Wallet class.



.. code-block:: bash

      >>> import pybgl
      >>> w=pybgl.Wallet(path_type='BIP84')
      >>> w.mnemonic
      'wet talent menu also ill comic smart unfold bone tape settle kangaroo caught tree wrap write diagram stomach have time addict unknown cruise polar'
      >>> w.account_private_xkey
      'zprvAchpNzD1oB4ndfzR6UBSeaFLuP2fNvbqsoP1PAfTwTLPESD8AFBbXigaoYzaZBjkJSxeYEXGQaVHzwZeSVYWCtX82GScZ9MwPYCmhBCFzJs'
      >>> w.account_public_xkey
      'zpub6qhAnVjudYd5rA4tCViT1iC5TQs9nPKhF2JcBZ55VnsN7EYGhnVr5X14enqueqWuz2nBBaDr77WT1Rnx82R1mTAbr9FbJq8oNdcf8UgndVA'
      >>> w=pybgl.Wallet('wet talent menu also ill comic smart unfold bone tape settle kangaroo caught tree wrap write diagram stomach have time addict unknown cruise polar',path_type='BIP84')
      >>> w.account_private_xkey
      'zprvAchpNzD1oB4ndfzR6UBSeaFLuP2fNvbqsoP1PAfTwTLPESD8AFBbXigaoYzaZBjkJSxeYEXGQaVHzwZeSVYWCtX82GScZ9MwPYCmhBCFzJs'
      >>> w.account_public_xkey
      'zpub6qhAnVjudYd5rA4tCViT1iC5TQs9nPKhF2JcBZ55VnsN7EYGhnVr5X14enqueqWuz2nBBaDr77WT1Rnx82R1mTAbr9FbJq8oNdcf8UgndVA'
      >>>





Get wallet addresses
--------------------


.. code-block:: bash

       >>> w.get_address(0)['address']
      'bgl1qjc46yw4zgggj4e0x6ew6htuu234j4y9vds66e2'
       >>> w.get_address(0)['private_key']
      'L1U3Fviv4PGDxQatgXimWnU8yLy6jVz12wAyxjjP4XLyjDx7aycU'
       >>> w.get_address(0)['public_key']
      '037269845622edcc243d7b203de508c899c33963e1e2d45a47884b7df5ab4be1ce'
       >>> w.get_address(1)['address']
       'bgl1qxepx0uqdu696vjwvszcel3r8lzss9m0htq6n8u'
       >>> w.get_address(1)['private_key']
       'KxGZ8JWxZpjBsz1QERdnrBRT2THEVkjr7q8fqCrJ7bFN1ys7EKPi'
       >>> w.get_address(1)['public_key']
       '03739adff69d48d2f8bac2bfacfbb1dcf6264fad4e67761c1d6890bde7ed858571'
       >>>