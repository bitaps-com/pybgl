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
      >>> # create P2PKH legacy format
      >>> pybgl.Address(address_type="P2PKH").address
      '1FGruSGTHj5WVDe8G8G2dJgkLyTMizHo8G'
      >>>
      >>> # create testnet address
      >>> pybgl.Address(address_type="P2PKH", testnet=True).address
      'n1giVCK9XA9FfDAVuNtDEeHJhH4aaNbMPq'
      >>>
      >>> # create P2SH_P2WPKH SEGWIT adoption address
      >>> pybgl.Address(address_type="P2SH_P2WPKH").address
      '32UHE8g2XFvhC6FTKkERtdkeuQYikZNsWR'
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

Get public key from private key

.. code-block:: bash

      >>> import pybgl
      >>> pybgl.private_to_public_key('5JCnJEggRKX5rscdGiqasmYdsyQ2fCYyLA7xYqSDRLEbWY7mZtq')
      '04153e10a2c18ffe097d10d431023590d22508765509fc74f6fd504bea9442e0ad0782ec8c446d82e40cec6e04981c016e39fca1d50009f2008cbe9621a05ddb72'
      >>>
      >>> pybgl.public_key_to_address('04153e10a2c18ffe097d10d431023590d22508765509fc74f6fd504bea9442e0ad0782ec8c446d82e40cec6e04981c016e39fca1d50009f2008cbe9621a05ddb72')
      >>>
      >>> # this is uncompressed public key, so we can't create witness address
      >>> # we have to set witness_version to None to get non segwit address
      >>> pub = pybgl.private_to_public_key('5JCnJEggRKX5rscdGiqasmYdsyQ2fCYyLA7xYqSDRLEbWY7mZtq')
      >>> pybgl.public_key_to_address(pub, witness_version=None)
      '1Nj5GErZy4Q58XEEJPwh5ZiFVKpp2BRSxZ'
      >>>

Tools

.. code-block:: bash

      >>> pybgl.is_address_valid('1Nj5GErZy4Q58XEEJPwh5ZiFVKpp2BRSxZ')
      True
      >>> pybgl.address_type('1Nj5GErZy4Q58XEEJPwh5ZiFVKpp2BRSxZ')
      'P2PKH'
      >>> pybgl.address_net_type('1Nj5GErZy4Q58XEEJPwh5ZiFVKpp2BRSxZ')
      'mainnet'
      >>>








