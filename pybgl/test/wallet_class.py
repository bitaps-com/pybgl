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

    def test_wallet_from_xpriv_key(self):
        w = Wallet(
            "xprv9s21ZrQH143K3V76RxiKKREaBYgPkxDtJk2JFZeKT5oUWM5odhxf6VVKWcWYsxkn8zthgTxaxZ4ao5MDuoQ3AxxkZErhAY86wN"
            "fkCGn9MTa")
        assert w.master_private_xkey == "xprv9s21ZrQH143K3V76RxiKKREaBYgPkxDtJk2JFZeKT5oUWM5odhxf6VVKWcWYsxkn8zthgTxaxZ4ao5MDuoQ3AxxkZErhAY86wNfkCGn9MTa"
        assert w.account_private_xkey == "xprv9xy9pW6QriePuzgpsBLoRjSE5ZhzVpdkPNF4377deALRSQ4RJRfBDvfz2XuqHNYSHy175udJTUodKeYWusgqbK4sTuhb1EoB1mcWzKFQR4u"
        assert w.account_public_xkey == "xpub6BxWE1dJh6Ch8UmHyCsonsNxdbYUuHMbkbAeqVXFCVsQKCPZqxyRmizTsr6d6WvfJpNSnUQy2yi9d6jZVSR5NzgaXjYqn95J93yQC5PqkZk"
        assert w.external_chain_private_xkey == "xprvA1LwXrHHrvp1QRhKRBkG82YoUKZmsmn887gH7fhgWYSc135bSdDdU7rhe73pkc95S24kL88vTXdQyjyNzAETQWkU2SBXn7zqJQgZgAvosx1"
        assert w.external_chain_public_xkey == "xpub6ELHwMpBhJNJcumnXDHGVAVY2MQGHEVyVLbsv47J4syasqQjzAXt1vBBVN8s1jxTKniP4NypmswJBsGK1PQQ49WvvrDNUtHYN8h9SX24nuV"
        assert w.internal_chain_private_xkey == "xprvA1LwXrHHrvp1Ub1i8zPEd7WPqmnbmd8K2dXihAqmdew6FaMSLMGdStw3UwjFsXYtngpoJoK4CwzV8GEBpCxDQeA54pY2XEy55qHVqWhWpDi"
        assert w.internal_chain_public_xkey == "xpub6ELHwMpBhJNJh56BF1vEzFT8Pod6B5rAPrTKVZFPBzU58NgastaszhFXLBchcsuNwTZLrVgcAJGvrHRQBA33B3UcbRqWwYg3AVhVn7MoCzv"
        assert w.path == "m/44'/0'/0'/0"
        assert w.path_type == "BIP44"
        assert w.depth == 0

        w = Wallet(
            "yprvABrGsX5C9jantnJDGKVwXWL5MWpqhaDPDrYX2xYCq6BMZSu2tN8DiZ9TXpU8ssQhYe1WRwZ9RDR8gMxndVp3yCeMRaZ7kSwbD6"
            "jPaq7NqCU")

        assert w.master_private_xkey == "yprvABrGsX5C9jantnJDGKVwXWL5MWpqhaDPDrYX2xYCq6BMZSu2tN8DiZ9TXpU8ssQhYe1WRwZ9RDR8gMxndVp3yCeMRaZ7kSwbD6jPaq7NqCU"
        assert w.account_private_xkey == "yprvAKNoUVXZ3WtAnEuayKC5MnMSVvLqAjcrWb5n4FB5Mp5QHv2nQrFDNj8nAwx5kgiNPEZVgJmJhCK" \
                                         "24axgrvH47oFSMzeB2E1jP9wtYYt4k55"
        assert w.account_public_xkey == "ypub6YN9t14SstSTziz45Lj5ivJB3xBKaCLhsp1Nrdagv9cPAiMvxPZTvXTG2D6jnsmGUUK13bDkDVEQ" \
                                        "u4F2DQpRcd72vHBb2neDf9TRAm9E7K6"
        assert w.external_chain_private_xkey == "yprvAKfNZUdQw7jVb7mt1b6CCE6b4VCwU35yW5DesrvBLJZhejkg1k6fnJhr4vrzcknzooULN" \
                                                "WwGxi8eMgB6susaX4RiXfr7SU4tAd3yvy2rmag"
        assert w.external_chain_public_xkey == "ypub6YeixzAJmVHnobrM7cdCZN3KcX3RsVopsJ9FgFKnte6gXY5pZHQvL72KvCjRBxdAzXsQa" \
                                               "ii7CcPTooRrKeNDMe1fVaD3Z8DGinm58vgNV2z"
        assert w.internal_chain_private_xkey == "yprvAKfNZUdQw7jVdSM6BKgtELaDfCrhRgzHxFvnAfH26LxoE9jYYfybQGruxS2NezefRyEe" \
                                                "H2s7oaj3LDarxRuqgQcPE5GHfZD6GgKLfWXaYvp"
        assert w.internal_chain_public_xkey == "ypub6YeixzAJmVHnqvRZHMDtbUWxDEhBq9i9KUrNy3gdegVn6x4h6DHqx5BPoisYumVWgsM5f" \
                                               "3ByH6bRVaLvJRfFKczg2QnRYBhWDEsQS7X8N73"
        assert w.path == "m/49'/0'/0'/0"
        assert w.path_type == "BIP49"
        assert w.depth == 0

        w = Wallet(
            "zprvAWgYBBk7JR8Gk5VL6gHZjbRaXUyHeCCt8y4jpMS6D6ZEcYiG92HnLcobZ2Risn4cxH8KBR9hssmgZeaMMCE4mSKxHvFYLMm5Upo2yQjkycx")
        assert w.master_private_xkey == "zprvAWgYBBk7JR8Gk5VL6gHZjbRaXUyHeCCt8y4jpMS6D6ZEcYiG92HnLcobZ2Risn4cxH8KBR9hssmgZeaMMCE4mSKxHvFYLMm5Upo2yQjkycx"
        assert w.account_private_xkey == "zprvAdMf8RaFvFUw8khtWvUimWvGQVSkBHMgacfBvD9VmLQpGDLVtp1jv51bV3wmJLg54dqm9FDfMEHjd5TYpGFdLmVof8akvPsXM33GQ7NP2GM"
        assert w.account_public_xkey == "zpub6rM1Xw79kd3EMEnMcx1j8erzxXHEak5XwqanibZ7Kfwo91feSMKzTsL5LLQFCXTRs6sBpnvis1S7eii3F9y2btCPLXHQMe7h4KoMzLu33Ss"
        assert w.external_chain_private_xkey == "zprvAfRpmUXV8Bx8m14g129H28qNFL9DJ8GTNS2QqhqhgQ25mEo43oYKCHEn3sYFQb4mPfEU5QnwKZZui1z5fDy4h42sb3PDjYeiDfPUGDtCH8n"
        assert w.external_chain_public_xkey == "zpub6tRBAz4NxZWRyV9973gHPGn6oMyhhazJjex1e6FKEjZ4e38CbLrZk5ZFu8sEEWShqfmkuiQ8gs2nXBTr2fEGf2iGE12oRvzbreG7kkZL6rW"
        assert w.internal_chain_private_xkey == "zprvAfRpmUXV8Bx8osLms5d2EidSqJuhHMhcZUpao9zjrYE1aayF9BkHMX5DgnYtkHPsnoiEwVYasn1tW9xArUXkwMvB4tEx7A9Df752CLGkPPt"
        assert w.internal_chain_public_xkey == "zpub6tRBAz4NxZWS2MREy7A2braBPLkBgpRTvhkBbYQMQskzTPJPgj4XuKPhY2ytqVcWVMHj1HJQUKkD1JXiuMvPNKLyEQcRLsxbrV49Lsu2K6f"
        assert w.path == "m/84'/0'/0'/0"
        assert w.path_type == "BIP84"
        assert w.depth == 0

        w = Wallet(
            "xprv9s21ZrQH143K3V76RxiKKREaBYgPkxDtJk2JFZeKT5oUWM5odhxf6VVKWcWYsxkn8zthgTxaxZ4ao5MDuoQ3AxxkZErhAY86wNfkCGn9MTa",
            path="m/0'/0'")
        assert w.master_private_xkey == "xprv9s21ZrQH143K3V76RxiKKREaBYgPkxDtJk2JFZeKT5oUWM5odhxf6VVKWcWYsxkn8zthgTxaxZ4ao5MDuoQ3AxxkZErhAY86wNfkCGn9MTa"
        assert w.chain_private_xkey == "xprv9xQsQ3WwFzzrPLvoafdumL9AV5fF6o74fGXLi3X7ByziXa11EFrYFwjC17BcNozBYY6p6f4ue7Cq2DCDd29dpYAwBecUR3hef63Xsjcsv2t"
        assert w.chain_public_xkey == "xpub6BQDoZ3q6NZ9bq1GghAv8U5u37VjWFpv2VSwWRvikKXhQNL9moAnok3frPogvw8GsN5T2ULjz4YoRPBVWi1EY9fGQpazwtQArRrYEHc8diy"
        assert w.path == "m/0'/0'"
        assert w.path_type == "custom"
        assert w.depth == 0

        w = Wallet(
            "xprv9s21ZrQH143K3V76RxiKKREaBYgPkxDtJk2JFZeKT5oUWM5odhxf6VVKWcWYsxkn8zthgTxaxZ4ao5MDuoQ3AxxkZErhAY86wNfkCGn9MTa",
            path="m/0'/0'")
        assert w.master_private_xkey == "xprv9s21ZrQH143K3V76RxiKKREaBYgPkxDtJk2JFZeKT5oUWM5odhxf6VVKWcWYsxkn8zthgTxaxZ4ao5MDuoQ3AxxkZErhAY86wNfkCGn9MTa"
        assert w.chain_private_xkey == "xprv9xQsQ3WwFzzrPLvoafdumL9AV5fF6o74fGXLi3X7ByziXa11EFrYFwjC17BcNozBYY6p6f4ue7Cq2DCDd29dpYAwBecUR3hef63Xsjcsv2t"
        assert w.chain_public_xkey == "xpub6BQDoZ3q6NZ9bq1GghAv8U5u37VjWFpv2VSwWRvikKXhQNL9moAnok3frPogvw8GsN5T2ULjz4YoRPBVWi1EY9fGQpazwtQArRrYEHc8diy"
        assert w.path == "m/0'/0'"
        assert w.path_type == "custom"
        assert w.depth == 0

        # from non master private key
        w = Wallet(
            "zprvAdMf8RaFvFUw8khtWvUimWvGQVSkBHMgacfBvD9VmLQpGDLVtp1jv51bV3wmJLg54dqm9FDfMEHjd5TYpGFdLmVof8akvPsXM33GQ7NP2GM")
        assert w.master_private_xkey is None
        assert w.account_private_xkey == "zprvAdMf8RaFvFUw8khtWvUimWvGQVSkBHMgacfBvD9VmLQpGDLVtp1jv51bV3wmJLg54dqm9FDfMEHjd5TYpGFdLmVof8akvPsXM33GQ7NP2GM"
        assert w.account_public_xkey == "zpub6rM1Xw79kd3EMEnMcx1j8erzxXHEak5XwqanibZ7Kfwo91feSMKzTsL5LLQFCXTRs6sBpnvis1S7eii3F9y2btCPLXHQMe7h4KoMzLu33Ss"
        assert w.external_chain_private_xkey == "zprvAfRpmUXV8Bx8m14g129H28qNFL9DJ8GTNS2QqhqhgQ25mEo43oYKCHEn3sYFQb4mPfEU5QnwKZZui1z5fDy4h42sb3PDjYeiDfPUGDtCH8n"
        assert w.external_chain_public_xkey == "zpub6tRBAz4NxZWRyV9973gHPGn6oMyhhazJjex1e6FKEjZ4e38CbLrZk5ZFu8sEEWShqfmkuiQ8gs2nXBTr2fEGf2iGE12oRvzbreG7kkZL6rW"
        assert w.internal_chain_private_xkey == "zprvAfRpmUXV8Bx8osLms5d2EidSqJuhHMhcZUpao9zjrYE1aayF9BkHMX5DgnYtkHPsnoiEwVYasn1tW9xArUXkwMvB4tEx7A9Df752CLGkPPt"
        assert w.internal_chain_public_xkey == "zpub6tRBAz4NxZWS2MREy7A2braBPLkBgpRTvhkBbYQMQskzTPJPgj4XuKPhY2ytqVcWVMHj1HJQUKkD1JXiuMvPNKLyEQcRLsxbrV49Lsu2K6f"
        assert w.path == "m/84'/0'/0'/0"
        assert w.path_type == "BIP84"
        assert w.depth == 3

    def test_wallet_from_xpub_key(self):
        w = Wallet(
            "xpub6BxWE1dJh6Ch8UmHyCsonsNxdbYUuHMbkbAeqVXFCVsQKCPZqxyRmizTsr6d6WvfJpNSnUQy2yi9d6jZVSR5NzgaXjYqn95J93yQC5PqkZk")
        assert w.account_public_xkey == "xpub6BxWE1dJh6Ch8UmHyCsonsNxdbYUuHMbkbAeqVXFCVsQKCPZqxyRmizTsr6d6WvfJpNSnUQy2yi9d6jZVSR5NzgaXjYqn95J93yQC5PqkZk"
        assert w.external_chain_public_xkey == "xpub6ELHwMpBhJNJcumnXDHGVAVY2MQGHEVyVLbsv47J4syasqQjzAXt1vBBVN8s1jxTKniP4NypmswJBsGK1PQQ49WvvrDNUtHYN8h9SX24nuV"
        assert w.internal_chain_public_xkey == "xpub6ELHwMpBhJNJh56BF1vEzFT8Pod6B5rAPrTKVZFPBzU58NgastaszhFXLBchcsuNwTZLrVgcAJGvrHRQBA33B3UcbRqWwYg3AVhVn7MoCzv"
        assert w.path == "m/44'/0'/0'/0"
        assert w.path_type == "BIP44"
        assert w.depth == 3

        w = Wallet(
            "ypub6YN9t14SstSTziz45Lj5ivJB3xBKaCLhsp1Nrdagv9cPAiMvxPZTvXTG2D6jnsmGUUK13bDkDVEQu4F2DQpRcd72vHBb2neDf9TRAm9E7K6")
        assert w.account_public_xkey == "ypub6YN9t14SstSTziz45Lj5ivJB3xBKaCLhsp1Nrdagv9cPAiMvxPZTvXTG2D6jnsmGUUK13bDkDVEQu4F2DQpRcd72vHBb2neDf9TRAm9E7K6"
        assert w.external_chain_public_xkey == "ypub6YeixzAJmVHnobrM7cdCZN3KcX3RsVopsJ9FgFKnte6gXY5pZHQvL72KvCjRBxdAzXsQaii7CcPTooRrKeNDMe1fVaD3Z8DGinm58vgNV2z"
        assert w.internal_chain_public_xkey == "ypub6YeixzAJmVHnqvRZHMDtbUWxDEhBq9i9KUrNy3gdegVn6x4h6DHqx5BPoisYumVWgsM5f3ByH6bRVaLvJRfFKczg2QnRYBhWDEsQS7X8N73"
        assert w.path == "m/49'/0'/0'/0"
        assert w.path_type == "BIP49"
        assert w.depth == 3

        w = Wallet(
            "zpub6rM1Xw79kd3EMEnMcx1j8erzxXHEak5XwqanibZ7Kfwo91feSMKzTsL5LLQFCXTRs6sBpnvis1S7eii3F9y2btCPLXHQMe7h4KoMzLu33Ss")
        assert w.account_public_xkey == "zpub6rM1Xw79kd3EMEnMcx1j8erzxXHEak5XwqanibZ7Kfwo91feSMKzTsL5LLQFCXTRs6sBpnvis1S7eii3F9y2btCPLXHQMe7h4KoMzLu33Ss"
        assert w.external_chain_public_xkey == "zpub6tRBAz4NxZWRyV9973gHPGn6oMyhhazJjex1e6FKEjZ4e38CbLrZk5ZFu8sEEWShqfmkuiQ8gs2nXBTr2fEGf2iGE12oRvzbreG7kkZL6rW"
        assert w.internal_chain_public_xkey == "zpub6tRBAz4NxZWS2MREy7A2braBPLkBgpRTvhkBbYQMQskzTPJPgj4XuKPhY2ytqVcWVMHj1HJQUKkD1JXiuMvPNKLyEQcRLsxbrV49Lsu2K6f"
        assert w.path == "m/84'/0'/0'/0"
        assert w.path_type == "BIP84"
        assert w.depth == 3

        w = Wallet(
            "xpub661MyMwAqRbcFyBZXzFKgZBJjaWtAQwjfxwu3x3w1RLTP9QxBFGueHooMvsC5tyAcZKpMzxNVUHx1PpZayH74UUHfDMTK9sJ5NZMjB8fMeE",
            path="m")
        assert w.chain_public_xkey == "xpub661MyMwAqRbcFyBZXzFKgZBJjaWtAQwjfxwu3x3w1RLTP9QxBFGueHooMvsC5tyAcZKpMzxNVUHx1PpZayH74UUHfDMTK9sJ5NZMjB8fMeE"
        assert w.path == "m"
        assert w.path_type == "custom"
        assert w.depth == 0

    def test_wallet_from_mnemonic(self):
        w = Wallet(
            "diary fresh float ostrich clean path tooth battle rebel nerve blood shock vital travel poet profit oval super lens purse army girl protect select")
        assert w.master_private_xkey == "zprvAWgYBBk7JR8Gj6Fyh7avt7VXDTaKuFtEUVYfanib1btw1hR5DNsbmpAJQuH8wXje8oCBAh182uNsu78TSW5DEm7DHXGugYYCzX571phh8sd"
        assert w.account_private_xkey == "zprvAds6aiRSB28DPqfPXm381XhejQT74yrcMYFVxKUq3RN6zdfHYhe2kdCfMVN6xizS6TjM2e9usWXBFAfzyof3jEpuw1SBbaN9ZeLTVnifWcN"
        assert w.account_public_xkey == "zpub6rrSzDxL1PgWcKjrdna8NfePHSHbUSaTimB6khtSbku5sRzS6ExHJRX9CnQ3YZc5mFDpq3cccw3Pt9KpoX2irELqhMEuzRpaLYqnrhqXqtR"
        assert w.external_chain_private_xkey == "zprvAfHTy9snayGyFCFZpHPuGDVTDhiQSAPU1yPT5Q8W6vnzAFoYP3yXDVCcGRUVw74SUXL9MBh4YEovtjyHymr2jnE9J3EFpqHjJmN9mp7cFWq"
        assert w.external_chain_public_xkey == "zpub6tGpNfQgRLqGTgL2vJvudMSBmjYtqd7KPCK3snY7fGKy348gvbHmmHX67imLvMRewEGMVL45oJdWk47B1ykpZSPAcYCf1Yajphh23MoAoSM"
        assert w.internal_chain_private_xkey == "zprvAfHTy9snayGyHoJXhR8ASoqSyQ2kuJx9yAPKVjdBTT6c47zKktR19sjXkzbumvB6S9Yh6PdYgXCZszypCmtrvjrBTCi7dy488mfdZFMpYQy"
        assert w.internal_chain_public_xkey == "zpub6tGpNfQgRLqGWHNzoSfAownBXRsFJmg1LPJvJ82o1ndavvKUJRjFhg41cGEYXjVDqx5MGb122nSDdSykH1GKa4Cm6ADZBg8MiwputCcQgHv"
        assert w.path == "m/84'/0'/0'/0"
        assert w.path_type == "BIP84"
        assert w.depth == 0


        m = "piano rookie mystery unit boil shoot short amazing average minute jewel wash country fortune attend idle mimic timber mobile music crater fly curve idea"

        s = [
            "flash fresh ride injury grit employ attack best mimic cycle main speak spawn apart found hole armor improve avocado volume clock arm indicate level",
            "arrow ranch theory urban coach curtain must album age fix nothing crane leg ritual engine flower invite energy monster design spy scrap harsh absorb"]
        w = Wallet(s)
        assert w.mnemonic == "piano rookie mystery unit boil shoot short amazing average minute jewel wash country fortune attend idle mimic timber mobile music crater fly curve idea"

        s = [
            "stool strong lecture client pioneer body lyrics ripple loan lucky country hill magnet angry welcome wealth spice minimum trouble decide involve sustain brave patient",
            "notable bundle mystery ice wise vicious photo meat embody kitchen crash wealth copy measure cloth squirrel acid pelican gown nut switch invest menu tide",
            "judge viable april siren spike circle disagree gospel seven south decide punch frozen despair decide maze slim limit federal opera quit atom logic gauge"]
        w = Wallet(s)
        assert w.mnemonic == "piano rookie mystery unit boil shoot short amazing average minute jewel wash country fortune attend idle mimic timber mobile music crater fly curve idea"

        s = [
            "alert tomorrow sudden charge earn minor airport mechanic jar employ dinner similar convince note scout welcome about slender nice inner arctic inside session list",
            "warm hidden junior best thank property myself such today age common left adapt copper gate people moment guide chef razor paper click throw actor",
            "aisle typical knock trumpet interest quantum isolate sudden outdoor noble enrich impulse sadness near battle razor bag grit airport ensure inject indicate grit sea",
            "dice flower wet quit wear success confirm have attitude give receive humble oak language multiply body spend element recipe warm congress index come select",
            "grit sheriff ketchup earth rail fix romance family check broom hand uncle sample what insect dash rapid exile blade evoke oil pass maze sentence"]
        w = Wallet(s)
        assert w.mnemonic == "piano rookie mystery unit boil shoot short amazing average minute jewel wash country fortune attend idle mimic timber mobile music crater fly curve idea"

        m = "diary fresh float ostrich clean path tooth battle rebel nerve blood shock vital travel poet profit oval super lens purse army girl protect select"
        w = Wallet(m, path="BIP44")
        assert w.path == "m/44'/0'/0'/0"
        assert w.master_private_xkey == "xprv9s21ZrQH143K2Vsk2Q1gTwJWsXHS21uEeGWE1zvpFb9AuVnci4YUXgr2NVMxwiRoKWxZfjp17afn8XuL17FBeHk1Yqt4WiuET4wpEcwY7ku"
        assert w.account_private_xkey == "xprv9zHPDQ6wBZ4QzGCNzsjKpEMG6PgQZ8C7esLQRLjqZj22rbeaTc1cQ39hj9oRkFT5zs2yJwdTNnnjqTqp2i1gGod4cShNEJrkFf92rtcvm1r"
        assert w.account_public_xkey == "xpub6DGjcudq1vciCkGr6uGLBNHzeRWtxauy26G1Dj9T84Z1jPyj19KrwqUBaS1cSJTMJwTn7pwiGae2vf5GyjXGaF2VMc1mrX6eavUARaiZoiY"
        assert w.external_chain_private_xkey == "xprvA1PF3AySergC7tBPGw3y6Q7b5hwBu26Av7TTmfF2xRKg283YiWuAY8a7WYmXja26cjU19nXwFCKGeqVUFnYggQ8TbJ7DSJkZLDA6mYMxH2o"
        assert w.external_chain_public_xkey == "xpub6ENbSgWLVEEVLNFrNxayTY4KdjmgJUp2HLP4a3eeWkretvNhG4DR5vtbMq2UfT1yGDmrkfy2Df4c4tCpGCUj7dGCvAuCea3GsznkzfwVT1p"
        assert w.internal_chain_private_xkey == "xprvA1PF3AySergC9m5gadK9JQdCHMBfpGUEsqdD2rP7vxoqDudvLPDrZsJc2ZeeLHhLQ5A94v2updumYivjRhWXxyyT4Ad8DNMDKkkvyLaDJQj"
        assert w.internal_chain_public_xkey == "xpub6ENbSgWLVEEVNFA9ger9fYZvqP2ADjC6F4YoqEnjVJLp6hy4svY77fd5sqJ573XNTQ1LTnQQiRj2MWMdoGm2CW3CANLZyquGASx2dURRKD8"
        assert w.path_type == "BIP44"
        assert w.depth == 0
        assert w.get_address(0)["private_key"] == "L45mfkreqWrCfjdttVv7WU69MSmmw38FZvcSwg66thqm9J9PK9KZ"
        assert w.get_address(0)["public_key"] == "02a933ce23a6b48dfb4621e8c71cc1541993318ce667c569b8affd2278ac24aa84"
        assert w.get_address(0)["address"] == "58efFj35hwDvCg2F5ya3vSPvsZb6Hx6VyK"
        assert w.get_address(0, False)["address"] == "5N6PRs4ZFMAbo3JKnkT5pGSk2XrYVgLs99"

        w = Wallet(m, path="BIP49")
        assert w.path == "m/49'/0'/0'/0"
        assert w.get_address(0)["address"] == "BGyhoKWNtuv6XQEUn3RT5Uoa3SSXytHk6X"
        assert w.get_address(0, False)["address"] == "B9GQMhusWLGddA5Ku12HUhw8hirC92WnUS"

        w = Wallet(m, path="BIP84")
        assert w.path == "m/84'/0'/0'/0"
        assert w.get_address(0)["address"] == "bgl1qk2k3lgzhpu227p9fvju6tnkxjxfrqef3cg3x5a"
        assert w.get_address(0, False)["address"] == "bgl1qaksfv2t58actx25pr9mnnavsnkxp5sp5lqx8we"

        w = Wallet(m, path="m/0'/0'")
        assert w.path == "m/0'/0'"
        assert w.get_address(0)["address"] == "5DKjzgnHZChshqDSMCboNP5o2DbEtsqi7C"

        w = Wallet(m, path="m/0'/0'", hardened_addresses=True)
        assert w.path == "m/0'/0'"
        assert w.get_address(0)["address"] == "5CnKYWo5GLPvgF131cFkfypmgoP8CZVbqG"

        v = "yprvABrGsX5C9januSiuGBeeAJRMQ2HACgKdfwFYPA4NAnwqqTz2BBERZpAJ1BwtcZWhb5tqbBHNRdSonfW3onhaKLy8FzsYGUUqfXdVdckvtMa"
        w = Wallet(v)
        assert w.get_address(0)["address"] == "BQ2J5V75ZJXhwjX4DfmEw3Bcvu7YHiDEg8"
        assert w.get_address(2147483707)["address"] == "BQRcB4YRStqRmh2op1MnTPqpW4JhW22UmG"
        assert w.get_address(2147483749)["address"] == "BM3U7MPBiXMJmLazZ2Xzvgpv8Fnc9ssZTy"
        assert w.get_address(2147483748)["address"] == "BL4z65x7nMtR8iPmrGimHEE9KfNnXYAC9v"
        v = "xpub6C74KmGmGX8NfwKHTVPD6EybguRsuDZpzq6rnxvxbCBBSs46U6AjuWuEs5YAD7eQeVE91aV1caZCUYzb5jcPCaRjuLdH5hbzKvHng5EyRvr"
        w = Wallet(v)
        assert w.get_address(0)["address"] == "5HJFtnfasQ8ELMSP7nzkEpfYsu5FWPFAXp"
        w = Wallet(v, path="m")
        assert w.get_address(0)["address"] == "5MuWdmYeM96gBg96qdoPKfAGQb97n6QDdG"


    def test_wallet_address_type(self):
        w = Wallet("tprv8ZgxMBicQKsPeuVhWwi6wuMQGfPKi9Li5GtX35jVNknACgqe3CY4g5xgkfDDJcmtF7o1QnxWDRYw4H5P26PXq7sbcUkEqeR4fg3Kxp2tigg",
            testnet=True, path="m/0'/0'", hardened_addresses=True)
        self.assertEqual(w.get_address(0, address_type='P2SH_P2WPKH')['address'],'MNdrJxcCUdaezMGfPHRUx5yqtsK9FyJXV1')
        self.assertEqual(w.get_address(1, address_type='P2SH_P2WPKH')['address'],'M7wuDjWEmiAFaAHiucfay543yFCvpH2FCd')
        self.assertEqual(w.get_address(0, address_type='P2WPKH')['address'],'tbgl1qrd3n235cj2czsfmsuvqqpr3lu6lg0ju7vtn4p8')
        self.assertEqual(w.get_address(1, address_type='P2WPKH')['address'],'tbgl1qfqeppuvj0ww98r6qghmdkj70tv8qpchet2y3pn')
        self.assertEqual(w.get_address(0, address_type='P2PKH')['address'],'EizKZyMWWBPkVTc5oqZFVHef8jLKDRCWCV')
        self.assertEqual(w.get_address(1, address_type='P2PKH')['address'],'Eo5F7AUY5ytK2dhA3tGLT3J4vPZ9aU18pR')




