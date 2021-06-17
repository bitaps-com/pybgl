import unittest
import os
import sys


parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from pybgl import  Wallet

class WalletClassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nTesting wallet class:\n")

    def test_is_wallet_menmonic(self):
        # mainnet
        m = "wet talent menu also ill comic smart unfold bone tape settle kangaroo caught tree wrap write diagram stomach have time addict unknown cruise polar"
        xpriv84 = "zprvAchpNzD1oB4ndfzR6UBSeaFLuP2fNvbqsoP1PAfTwTLPESD8AFBbXigaoYzaZBjkJSxeYEXGQaVHzwZeSVYWCtX82GScZ9MwPYCmhBCFzJs"
        xpub84 = "zpub6qhAnVjudYd5rA4tCViT1iC5TQs9nPKhF2JcBZ55VnsN7EYGhnVr5X14enqueqWuz2nBBaDr77WT1Rnx82R1mTAbr9FbJq8oNdcf8UgndVA"

        xpriv84root = "zprvAWgYBBk7JR8GjnuQxd7ebmSVGMoC5jFYenoAxFDio1w8SvmJaCkyKVVoU8kvCJ7PP6C6XT951t7Am2t1iPZPhzQrccQCS6WcVd4uBYKa7BE"

        a84_0 = "bgl1qjc46yw4zgggj4e0x6ew6htuu234j4y9vds66e2"
        a84_1 = "bgl1qxepx0uqdu696vjwvszcel3r8lzss9m0htq6n8u"

        p84_0 = "L1U3Fviv4PGDxQatgXimWnU8yLy6jVz12wAyxjjP4XLyjDx7aycU"
        p84_1 = "KxGZ8JWxZpjBsz1QERdnrBRT2THEVkjr7q8fqCrJ7bFN1ys7EKPi"


        w = Wallet(m, path_type="BIP84")
        self.assertEqual(w.testnet, False)
        self.assertEqual(w.account_public_xkey, xpub84)
        self.assertEqual(w.account_private_xkey, xpriv84)
        self.assertEqual(w.get_address(0)["address"], a84_0)
        self.assertEqual(w.get_address(1)["address"], a84_1)
        self.assertEqual(w.get_address(0)["private_key"], p84_0)
        self.assertEqual(w.get_address(1)["private_key"], p84_1)

        w2 = Wallet(xpub84)
        self.assertEqual(w2.testnet, False)
        self.assertEqual(w2.account_public_xkey, xpub84)
        self.assertEqual(w2.account_private_xkey, None)
        self.assertEqual(w2.get_address(0)["address"], a84_0)
        self.assertEqual(w2.get_address(1)["address"], a84_1)

        w3 = Wallet(xpriv84, path_type="BIP84")
        self.assertEqual(w3.testnet, False)
        self.assertEqual(w3.account_public_xkey, xpub84)
        self.assertEqual(w3.account_private_xkey, xpriv84)
        self.assertEqual(w3.get_address(0)["address"], a84_0)
        self.assertEqual(w3.get_address(1)["address"], a84_1)
        self.assertEqual(w3.get_address(0)["private_key"], p84_0)
        self.assertEqual(w3.get_address(1)["private_key"], p84_1)

        w3 = Wallet(xpriv84)
        self.assertEqual(w3.testnet, False)
        self.assertEqual(w3.account_public_xkey, xpub84)
        self.assertEqual(w3.account_private_xkey, xpriv84)
        self.assertEqual(w3.get_address(0)["address"], a84_0)
        self.assertEqual(w3.get_address(1)["address"], a84_1)
        self.assertEqual(w3.get_address(0)["private_key"], p84_0)
        self.assertEqual(w3.get_address(1)["private_key"], p84_1)

        w3 = Wallet(xpriv84root)
        self.assertEqual(w3.testnet, False)
        self.assertEqual(w3.account_public_xkey, xpub84)
        self.assertEqual(w3.account_private_xkey, xpriv84)
        self.assertEqual(w3.get_address(0)["address"], a84_0)
        self.assertEqual(w3.get_address(1)["address"], a84_1)
        self.assertEqual(w3.get_address(0)["private_key"], p84_0)
        self.assertEqual(w3.get_address(1)["private_key"], p84_1)

        xpriv84root="tprv8ZgxMBicQKsPd7Uf69XL1XwhmjHopUGep8GuEiJDZmbQz6o58LninorQAfcKZWARbtRtfnLcJ5MQ2AtHcQJCCRUcMRvmDUjyEmNUWwx8UbK"
        w4 = Wallet(xpriv84root,"BIP44", testnet=True)

        w5 = Wallet(xpriv84root, "BIP49")

        w6 = Wallet(xpriv84root, "BIP84")




