
========================
Pure functions reference
========================

Base function primitives implemented in functional programming paradigm.



Mnemonic(BIP39)
===============

.. autofunction:: pybgl.generate_entropy
.. autofunction:: pybgl.load_word_list
.. autofunction:: pybgl.entropy_to_mnemonic
.. autofunction:: pybgl.mnemonic_to_entropy
.. autofunction:: pybgl.mnemonic_to_seed


Private keys
============

.. autofunction:: pybgl.create_private_key
.. autofunction:: pybgl.private_key_to_wif
.. autofunction:: pybgl.wif_to_private_key
.. autofunction:: pybgl.is_wif_valid


Public keys
===========

.. WARNING::
   Using uncompressed public keys is
   `deprecated <https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki#restrictions-on-public-key-type>`_
   in  a new SEGWIT address format.
   To avoid potential future funds loss, users MUST NOT use uncompressed keys
   in version 0 witness programs. Use uncompressed keys only for backward
   compatibilitylegacy in legacy address format (PUBKEY, P2PKH).


.. autofunction:: pybgl.private_to_public_key
.. autofunction:: pybgl.is_public_key_valid



Extended keys(BIP32)
====================

.. autofunction:: pybgl.create_master_xprivate_key
.. autofunction:: pybgl.xprivate_to_xpublic_key
.. autofunction:: pybgl.derive_xkey
.. autofunction:: pybgl.public_from_xpublic_key
.. autofunction:: pybgl.private_from_xprivate_key



Addresses
=========

.. autofunction:: pybgl.hash_to_address
.. autofunction:: pybgl.address_to_hash
.. autofunction:: pybgl.public_key_to_address
.. autofunction:: pybgl.address_type
.. autofunction:: pybgl.address_to_script
.. autofunction:: pybgl.is_address_valid



Script
======

.. autofunction:: pybgl.decode_script
.. autofunction:: pybgl.parse_script
.. autofunction:: pybgl.delete_from_script
.. autofunction:: pybgl.script_to_hash


Signatures
==========

.. autofunction:: pybgl.verify_signature
.. autofunction:: pybgl.sign_message
.. autofunction:: pybgl.is_valid_signature_encoding


Hash encoding
=============

.. autofunction:: pybgl.rh2s
.. autofunction:: pybgl.s2rh
.. autofunction:: pybgl.reverse_hash


Merkle root
===========

.. autofunction:: pybgl.merkle_root
.. autofunction:: pybgl.merkle_branches
.. autofunction:: pybgl.merkleroot_from_branches


Difficulty
==========

.. autofunction:: pybgl.bits_to_target
.. autofunction:: pybgl.target_to_difficulty
.. autofunction:: pybgl.bits_to_difficulty
.. autofunction:: pybgl.difficulty_to_target


Tools
=====

.. autofunction:: pybgl.bytes_needed
.. autofunction:: pybgl.int_to_bytes
.. autofunction:: pybgl.bytes_to_int
.. autofunction:: pybgl.int_to_var_int
.. autofunction:: pybgl.var_int_to_int
.. autofunction:: pybgl.var_int_len
.. autofunction:: pybgl.get_var_int_len
.. autofunction:: pybgl.read_var_int
.. autofunction:: pybgl.read_var_list
.. autofunction:: pybgl.int_to_c_int
.. autofunction:: pybgl.c_int_to_int
.. autofunction:: pybgl.c_int_len






