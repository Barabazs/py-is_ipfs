from is_ipfs import Validator
import cid
import unittest


class TestCase(unittest.TestCase):
    def test_is_cid(self):
        valid_strings_v0 = ["QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE7o"]
        invalid_strings_v0 = ["QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE70"]
        valid_strings_v1 = [
            "bafybeie2reiz2q6rbcuwpy2etyztjnceolu4rdi7rp3th2lsky4r5ckeey"
        ]
        invalid_strings_v1 = [
            "bafybeie2reiz2q6rbcuwpy2etyztjnceolu4rdi7rp3th2lsky4r5ckee"
        ]
        random_invalid_strings = [
            "",
            "dfmqjdmfkjqdm",
            "bafybeierhgbz4zp2x2u67urqrgfnrnlukciupzenpqpipiz5nwtq",
            "1234",
        ]

        with self.subTest("Test valid CIDv0 strings"):
            for string in valid_strings_v0:
                self.assertTrue(Validator(string)._is_CID())

        with self.subTest("Test invalid CIDv0 strings"):
            for string in invalid_strings_v0:
                self.assertFalse(Validator(string)._is_CID())

        with self.subTest("Test valid CIDv1 strings"):
            for string in valid_strings_v1:
                self.assertTrue(Validator(string)._is_CID())

        with self.subTest("Test invalid CIDv1 strings"):
            for string in invalid_strings_v1:
                self.assertFalse(Validator(string)._is_CID())

        with self.subTest("Test invalid misc input"):
            for string in random_invalid_strings:
                self.assertFalse(Validator(string)._is_CID())

        with self.subTest("Test valid CIDv0 objects"):
            for string in valid_strings_v0:
                self.assertTrue(Validator(cid.make_cid(string))._is_CID())

        # with self.subTest("Test invalid CIDv0 objects"):
        #     for string in invalid_strings_v0:
        #         self.assertFalse(is_ipfs.is_ipfs(cid.CIDv0(string)))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
