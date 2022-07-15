import unittest
import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from pybgl.functions import script as tools
from pybgl import functions
from pybgl import BYTE_OPCODE, HEX_OPCODE
from binascii import unhexlify, hexlify


class AddressFunctionsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nTesting address functions:\n")

    def test_private_key_to_WIF(self):
        p = "ceda1ae4286015d45ec5147fe3f63e9377ccd6d4e98bcf0847df9937da1944a4"
        pcm = "L49obCXV7fGz2YRzLCSJgeZBYmGeBbKPT7xiehUeYX2S4URkPFZX"
        pum = "5KPPLXhtga99qqMceRo4Z6LXV3Kx6a9hRx3ez2U7EwP5KZfy2Wf"
        put = "93A1vGXSGoDHotruGmgyRgtV8hgfFjgtmtuc4epcag886W9d44L"
        pct = "cUWo47XLYiyFByuFicFS3y4FAza3r3R5XA7Bm7wA3dgSKDYox7h6"
        self.assertEqual(functions.private_key_to_wif(p, compressed=1, testnet=0), pcm)
        self.assertEqual(functions.private_key_to_wif(p, compressed=0, testnet=0), pum)
        self.assertEqual(functions.private_key_to_wif(p, compressed=1, testnet=1), pct)
        self.assertEqual(functions.private_key_to_wif(p, compressed=0, testnet=1), put)

    def test_is_WIF_valid(self):
        self.assertEqual(functions.is_wif_valid("L49obCXV7fGz2YRzLCSJgeZBYmGeBbKPT7xiehUeYX2S4URkPFZX"), 1)
        self.assertEqual(functions.is_wif_valid("5KPPLXhtga99qqMceRo4Z6LXV3Kx6a9hRx3ez2U7EwP5KZfy2Wf"), 1)
        self.assertEqual(functions.is_wif_valid("5KPPLXhtga99qqMcWRo4Z6LXV3Kx6a9hRx3ez2U7EwP5KZfy2Wf"), 0)
        self.assertEqual(functions.is_wif_valid("93A1vGXSGoDHotruGmgyRgtV8hgfFjgtmtuc4epcag886W9d44L"), 1)
        self.assertEqual(functions.is_wif_valid("cUWo47XLYiyFByuFicFS3y4FAza3r3R5XA7Bm7wA3dgSKDYox7h6"), 1)
        self.assertEqual(functions.is_wif_valid("cUWo47XLYiyByuFicFS3y4FAza3r3R5XA7Bm7wA3dgSKDYox7h6"), 0)

    def test_WIF_to_private_key(self):
        p = "ceda1ae4286015d45ec5147fe3f63e9377ccd6d4e98bcf0847df9937da1944a4"
        self.assertEqual(functions.wif_to_private_key("L49obCXV7fGz2YRzLCSJgeZBYmGeBbKPT7xiehUeYX2S4URkPFZX",
                                                  hex=1),p)
        self.assertEqual(functions.wif_to_private_key("L49obCXV7fGz2YRzLCSJgeZBYmGeBbKPT7xiehUeYX2S4URkPFZX",
                                                  hex=0),unhexlify(p))
        self.assertEqual(functions.wif_to_private_key("5KPPLXhtga99qqMceRo4Z6LXV3Kx6a9hRx3ez2U7EwP5KZfy2Wf",
                                                  hex=1),p)
        self.assertEqual(functions.wif_to_private_key("93A1vGXSGoDHotruGmgyRgtV8hgfFjgtmtuc4epcag886W9d44L",
                                                  hex=1),p)
        self.assertEqual(functions.wif_to_private_key("cUWo47XLYiyFByuFicFS3y4FAza3r3R5XA7Bm7wA3dgSKDYox7h6",
                                                  hex=1),p)

    def test_create_private_key(self):
        p = functions.create_private_key(wif=0)
        pw = functions.private_key_to_wif(p)
        self.assertEqual(functions.is_wif_valid(pw), True)



    def test_private_to_public_key(self):
        p = "ceda1ae4286015d45ec5147fe3f63e9377ccd6d4e98bcf0847df9937da1944a4"
        pu = "04b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4c8cbe28702911260f2a1da099a338bed4ee98f66bb8dba8031a76ab537ff6663"
        pk = "03b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4"
        self.assertEqual(functions.private_to_public_key(p, hex=1), pk)
        self.assertEqual(functions.private_to_public_key(p, hex=0), unhexlify(pk))
        self.assertEqual(functions.private_to_public_key(p, compressed=0, hex=1), pu)
        self.assertEqual(functions.private_to_public_key("L49obCXV7fGz2YRzLCSJgeZBYmGeBbKPT7xiehUeYX2S4URkPFZX", hex=1), pk)
        self.assertEqual(functions.private_to_public_key("5KPPLXhtga99qqMceRo4Z6LXV3Kx6a9hRx3ez2U7EwP5KZfy2Wf", hex=1), pu)
        self.assertEqual(functions.private_to_public_key("93A1vGXSGoDHotruGmgyRgtV8hgfFjgtmtuc4epcag886W9d44L", hex=1), pu)
        self.assertEqual(functions.private_to_public_key("cUWo47XLYiyFByuFicFS3y4FAza3r3R5XA7Bm7wA3dgSKDYox7h6", hex=1), pk)

    def test_hash_to_address(self):
        pc = "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
        h = tools.hash160(pc)
        s =  bytes([len(unhexlify(pc))])+unhexlify(pc) + BYTE_OPCODE["OP_CHECKSIG"]
        self.assertEqual(functions.hash_to_address(h), "bgl1qw508d6qejxtdg4y5r3zarvary0c5xw7k0fy5a3")
        self.assertEqual(functions.hash_to_address(h, testnet=1), "tbgl1qw508d6qejxtdg4y5r3zarvary0c5xw7kcm8awm")
        self.assertEqual(functions.hash_to_address(h, testnet=1, regtest=1), "rbgl1qw508d6qejxtdg4y5r3zarvary0c5xw7kahx879")
        h = tools.script_to_hash(s, 1, 1)
        self.assertEqual(functions.hash_to_address(h), "bgl1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qwkcqlq")
        self.assertEqual(functions.hash_to_address(h, testnet=1), "tbgl1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3q9eu7q4")
        pk = "03b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4"
        h = tools.hash160(pk)
        self.assertEqual(functions.hash_to_address(h, witness_version=None), "5HF4NvqdABfHLYyAtkrAbpzPb6rfiLaE7h")
        self.assertEqual(functions.hash_to_address(h, witness_version=None, testnet=1), "EwMY1XzYCWnJxxKFUpqpEqXGhD3Jme2MmH")
        # p2wpkh inside p2sh
        p = "L32a8Mo1LgvjrVDbzcc3NkuUfkpoLsf2Y2oEWkV4t1KpQdFzuyff"
        pk = functions.private_to_public_key(p)
        script = b'\x00\x14' + tools.hash160(pk)
        script_hash = tools.hash160(script)
        self.assertEqual(functions.hash_to_address(script_hash,
                                                   script_hash=1,
                                                   witness_version=None), "B6LphCnoPPtK8hyQQjCfKWRec8bhGTEmm7")
        self.assertEqual(functions.hash_to_address(script_hash,
                                                   script_hash=1,
                                                   witness_version=None,
                                                   testnet=1), "M9nuJvF18uUDaYTa2DXdSeEKLk3H3Tsw1e")

    def test_address_to_hash(self):
        h = "751e76e8199196d454941c45d1b3a323f1433bd6"
        self.assertEqual(functions.address_to_hash("bgl1qw508d6qejxtdg4y5r3zarvary0c5xw7k0fy5a3", 1), h)
        self.assertEqual(functions.address_to_hash("tbgl1qw508d6qejxtdg4y5r3zarvary0c5xw7kcm8awm", 1), h)
        h  = "1863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262"
        self.assertEqual(functions.address_to_hash("bgl1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qwkcqlq", 1), h)
        h = "a307d67484911deee457779b17505cedd20e1fe9"
        self.assertEqual(functions.address_to_hash("5HF4NvqdABfHLYyAtkrAbpzPb6rfiLaE7h", 1), h)
        self.assertEqual(functions.address_to_hash("EwMY1XzYCWnJxxKFUpqpEqXGhD3Jme2MmH", 1), h)
        h = "14c14c8d26acbea970757b78e6429ad05a6ac6bb"
        self.assertEqual(functions.address_to_hash("B6LphCnoPPtK8hyQQjCfKWRec8bhGTEmm7", 1), h)
        self.assertEqual(functions.address_to_hash("M9nuJvF18uUDaYTa2DXdSeEKLk3H3Tsw1e", 1), h)

    def test_address_type(self):
        self.assertEqual(functions.address_type("bgl1qw508d6qejxtdg4y5r3zarvary0c5xw7k0fy5a3"), 'P2WPKH')
        self.assertEqual(functions.address_type("tbgl1qw508d6qejxtdg4y5r3zarvary0c5xw7kcm8awm"), 'P2WPKH')
        self.assertEqual(functions.address_type("bgl1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qwkcqlq"), 'P2WSH')
        self.assertEqual(functions.address_type("tbgl1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3q9eu7q4"), 'P2WSH')
        self.assertEqual(functions.address_type("5HF4NvqdABfHLYyAtkrAbpzPb6rfiLaE7h"), 'P2PKH')
        self.assertEqual(functions.address_type("EwMY1XzYCWnJxxKFUpqpEqXGhD3Jme2MmH"), 'P2PKH')
        self.assertEqual(functions.address_type("B6LphCnoPPtK8hyQQjCfKWRec8bhGTEmm7"), 'P2SH')
        self.assertEqual(functions.address_type("M9nuJvF18uUDaYTa2DXdSeEKLk3H3Tsw1e"), 'P2SH')

    def test_address_net_type(self):
        self.assertEqual(functions.address_net_type("bgl1qw508d6qejxtdg4y5r3zarvary0c5xw7k0fy5a3"), 'mainnet')
        self.assertEqual(functions.address_net_type("tbgl1qw508d6qejxtdg4y5r3zarvary0c5xw7kcm8awm"), 'testnet')
        self.assertEqual(functions.address_net_type("bgl1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qwkcqlq"),
                         'mainnet')
        self.assertEqual(functions.address_net_type("tbgl1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3q9eu7q4"),
                         'testnet')
        self.assertEqual(functions.address_net_type("5HF4NvqdABfHLYyAtkrAbpzPb6rfiLaE7h"), 'mainnet')
        self.assertEqual(functions.address_net_type("EwMY1XzYCWnJxxKFUpqpEqXGhD3Jme2MmH"), 'testnet')
        self.assertEqual(functions.address_net_type("B6LphCnoPPtK8hyQQjCfKWRec8bhGTEmm7"), 'mainnet')
        self.assertEqual(functions.address_net_type("M9nuJvF18uUDaYTa2DXdSeEKLk3H3Tsw1e"), 'testnet')

    def test_public_key_to_address(self):
        pc = "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
        self.assertEqual(functions.public_key_to_address(pc), "bgl1qw508d6qejxtdg4y5r3zarvary0c5xw7k0fy5a3")
        self.assertEqual(functions.public_key_to_address(pc, testnet=1), "tbgl1qw508d6qejxtdg4y5r3zarvary0c5xw7kcm8awm")
        pc = "03b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4"
        self.assertEqual(functions.public_key_to_address(pc,
                                                     witness_version=None,
                                                     testnet=0), "5HF4NvqdABfHLYyAtkrAbpzPb6rfiLaE7h")
        self.assertEqual(functions.public_key_to_address(pc, witness_version=None,
                                                     testnet=1), "EwMY1XzYCWnJxxKFUpqpEqXGhD3Jme2MmH")
        p = "L32a8Mo1LgvjrVDbzcc3NkuUfkpoLsf2Y2oEWkV4t1KpQdFzuyff"
        pk = functions.private_to_public_key(p)
        self.assertEqual(functions.public_key_to_address(pk, p2sh_p2wpkh=1,
                                                     witness_version=None), "B6LphCnoPPtK8hyQQjCfKWRec8bhGTEmm7")

    def test_is_address_valid(self):
        self.assertEqual(functions.is_address_valid("bgl1qw508d6qejxtdg4y5r3zarvary0c5xw7k0fy5a3"), 1)
        self.assertEqual(functions.is_address_valid("tbgl1qw508d6qejxtdg4y5r3zarvary0c5xw7kcm8awm", 1), 1)
        self.assertEqual(functions.is_address_valid("tbgl1qw508d6qejxtdg4y5r3zarvary0c5xw7kcm8awm"), 0)
        self.assertEqual(functions.is_address_valid("bgl1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qwkcqlq"), 1)
        self.assertEqual(functions.is_address_valid("tbgl1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3q9eu7q4", 1), 1)
        self.assertEqual(functions.is_address_valid("5HF4NvqdABfHLYyAtkrAbpzPb6rfiLaE7h"), 1)
        self.assertEqual(functions.is_address_valid("EwMY1XzYCWnJxxKFUpqpEqXGhD3Jme2MmH", 1), 1)
        self.assertEqual(functions.is_address_valid("B6LphCnoPPtK8hyQQjCfKWRec8bhGTEmm7"), 1)
        self.assertEqual(functions.is_address_valid("M9nuJvF18uUDaYTa2DXdSeEKLk3H3Tsw1e",1), 1)
        self.assertEqual(functions.is_address_valid("bgl1qw508d6qejxtdg4y5r3zarvary0c5xw7k0fy5a3", 1), 0)
        self.assertEqual(functions.is_address_valid("tbgl1qw508d6qejxtdg4y5r3zarvary0c5xw7kcm8awm",1), 1)
        self.assertEqual(functions.is_address_valid("bgl1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qwkcql3"), 0)
        self.assertEqual(functions.is_address_valid("tbgl1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3q9eu7q2",1), 0)
        self.assertEqual(functions.is_address_valid("5HF4NvqdABfHLYyAtkrAbpzPb6rfiq5c36"), 0)
        self.assertEqual(functions.is_address_valid("EwMY1XzYCWnJxxKFUpqpEqXGhD3Jj6QTxX", 1), 0)
        self.assertEqual(functions.is_address_valid("B6LphCnoPPtK8hyQQjCfKWRec8bhJXgcrU"), 0)

    def test_address_to_script(self):
        self.assertEqual(functions.address_to_script("59ERgZdwPeXrXGDYv4v7jFvrj1bhSTiDYk", 1),
                         "76a9144b2832feeda5692c96c0594a6314136a998f515788ac")
        self.assertEqual(functions.address_to_script("BLn1jVFVtM4z6W5UMKyxeYSP3DVJPdW6pw", 1),
                         "a914b316ac9bdd0816ecdec6773d1192c0eaf52ae66487")
        self.assertEqual(functions.address_to_script("bgl1qw508d6qejxtdg4y5r3zarvary0c5xw7k0fy5a3", 1),
                         "0014751e76e8199196d454941c45d1b3a323f1433bd6")


    def test_parse_script(self):

        k = tools.parse_script("76a9144b2832feeda5692c96c0594a6314136a998f515788ac")
        address = functions.hash_to_address(k["addressHash"], witness_version = None)
        self.assertEqual(address, "59ERgZdwPeXrXGDYv4v7jFvrj1bhQMZsPF")
        self.assertEqual(k["type"],"P2PKH")
        self.assertEqual(k["nType"],0)
        self.assertEqual(k["reqSigs"],1)
        self.assertEqual(functions.address_to_script(address, 1),
                         "76a9144b2832feeda5692c96c0594a6314136a998f515788ac")

        k = tools.parse_script("76a914a307d67484911deee457779b17505cedd20e1fe988ac")
        address = functions.hash_to_address(k["addressHash"], testnet= True, witness_version=None)
        self.assertEqual(address,"EwMY1XzYCWnJxxKFUpqpEqXGhD3Jme2MmH")
        self.assertEqual(k["type"],"P2PKH")
        self.assertEqual(k["nType"],0)
        self.assertEqual(k["reqSigs"],1)
        self.assertEqual(functions.address_to_script(address, 1),
                         "76a914a307d67484911deee457779b17505cedd20e1fe988ac")

        k = tools.parse_script("a914b316ac9bdd0816ecdec6773d1192c0eaf52ae66487")
        address = functions.hash_to_address(k["addressHash"], script_hash=True, witness_version=None)
        self.assertEqual(address, "BLn1jVFVtM4z6W5UMKyxeYSP3DVJQVzgVT")
        self.assertEqual(k["type"],"P2SH")
        self.assertEqual(k["nType"],1)
        self.assertEqual(k["reqSigs"], None)
        self.assertEqual(functions.address_to_script(address, 1),
                         "a914b316ac9bdd0816ecdec6773d1192c0eaf52ae66487")

        k = tools.parse_script("0014751e76e8199196d454941c45d1b3a323f1433bd6")
        address = functions.hash_to_address(k["addressHash"], script_hash=False,
                                        witness_version=0, testnet=False)
        self.assertEqual(address, "bgl1qw508d6qejxtdg4y5r3zarvary0c5xw7k0fy5a3")
        self.assertEqual(k["type"],"P2WPKH")
        self.assertEqual(k["nType"],5)
        self.assertEqual(k["reqSigs"],1)
        self.assertEqual(functions.address_to_script(address, 1),
                         "0014751e76e8199196d454941c45d1b3a323f1433bd6")

        s = [HEX_OPCODE['OP_HASH160'],
             '14',
             '92c2f2da37093971ca335824edae06468e60ea20',
             HEX_OPCODE['OP_EQUAL']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        address = functions.hash_to_address(k["addressHash"], script_hash=True,
                                        witness_version=None, testnet=False)
        self.assertEqual(address, "BHq5ozUtze6DCm3ds23JVBbkotBoh7Uj3b")
        self.assertEqual(k["type"],"P2SH")
        self.assertEqual(k["nType"],1)
        self.assertEqual(k["reqSigs"], None)
        self.assertEqual(functions.address_to_script(address, 1), h)

        s = [HEX_OPCODE['OP_3'],
             '21',
             '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        sh = tools.script_to_hash(h, 0, 0)
        address = functions.hash_to_address(sh,script_hash=True,
                                        witness_version=None, testnet=False)
        self.assertEqual(address, "BFnsM4b97AkMkxB3G11aunzYRr8EjGkSYU")
        self.assertEqual(k["type"],"MULTISIG")
        self.assertEqual(k["nType"],4)
        self.assertEqual(k["reqSigs"],3)

        s = [HEX_OPCODE['OP_0'],
             '21',
             '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        sh = tools.script_to_hash(h, 0,0)
        self.assertEqual(k["type"],"NON_STANDARD")
        self.assertEqual(k["nType"],7)
        self.assertEqual(k["reqSigs"],20)

        s = [HEX_OPCODE['OP_1'],
             '21',
             '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        self.assertEqual(k["type"],"MULTISIG")
        self.assertEqual(k["nType"],4)
        self.assertEqual(k["reqSigs"],1)



        s = [HEX_OPCODE['OP_1'],
             HEX_OPCODE['OP_1'],
             '21',
             '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        sh = tools.script_to_hash(h, 0, 0)
        self.assertEqual(k["type"],"NON_STANDARD")
        self.assertEqual(k["nType"],7)
        self.assertEqual(k["reqSigs"],1)

        s = [HEX_OPCODE['OP_1'],
             HEX_OPCODE['OP_6'],
             '21',
             '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        self.assertEqual(k["type"], "NON_STANDARD")
        self.assertEqual(k["nType"], 7)
        self.assertEqual(k["reqSigs"], 6)

        s = [HEX_OPCODE['OP_1'],
             HEX_OPCODE['OP_6'],
             '21',
             '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        self.assertEqual(k["type"],"NON_STANDARD")
        self.assertEqual(k["nType"],7)
        self.assertEqual(k["reqSigs"],20)

        s = [HEX_OPCODE['OP_1'],
             HEX_OPCODE['OP_6'],
             '21',
             '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKSIG'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        self.assertEqual(k["type"],"NON_STANDARD")
        self.assertEqual(k["nType"],7)
        self.assertEqual(k["reqSigs"],21)


        s = [HEX_OPCODE['OP_1'],
             HEX_OPCODE['OP_6'],
             '21',
             '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        self.assertEqual(k["type"],"NON_STANDARD")
        self.assertEqual(k["nType"],7)
        self.assertEqual(k["reqSigs"],20)

        s = [
             HEX_OPCODE['OP_6'],
             '21',
             '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        self.assertEqual(k["type"],"NON_STANDARD")
        self.assertEqual(k["nType"],7)
        self.assertEqual(k["reqSigs"],20)


        s = [
             HEX_OPCODE['OP_6'],
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        self.assertEqual(k["type"],"MULTISIG")
        self.assertEqual(k["nType"],4)
        self.assertEqual(k["reqSigs"],6)


        s = [
             HEX_OPCODE['OP_1'],
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        self.assertEqual(k["type"],"MULTISIG")
        self.assertEqual(k["nType"],4)
        self.assertEqual(k["reqSigs"],1)



        s = [
             HEX_OPCODE['OP_1'],
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             '21',
             '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        self.assertEqual(k["type"],"NON_STANDARD")
        self.assertEqual(k["nType"],7)
        self.assertEqual(k["reqSigs"],20)


        s = [
             HEX_OPCODE['OP_1'],
             '21',
             '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
             '21',
             '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
             HEX_OPCODE['OP_DUP'],
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             '21',
             '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
             '21',
             '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
             HEX_OPCODE['OP_6'],
             HEX_OPCODE['OP_CHECKMULTISIG']]
        h = ''.join(s)
        s = unhexlify(h)
        k = tools.parse_script(s)
        self.assertEqual(k["type"],"NON_STANDARD")
        self.assertEqual(k["nType"],7)
        self.assertEqual(k["reqSigs"],20)

