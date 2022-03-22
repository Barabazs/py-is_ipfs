from is_ipfs import Validator
import cid
import unittest


class TestCase(unittest.TestCase):
    def test_is_ipfs(self):
        # Test valid CIDv0 strings
        self.assertTrue(
            Validator("QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE7o").is_ipfs()
        )
        # Test invalid CIDv0 strings
        self.assertFalse(
            Validator("QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE70").is_ipfs()
        )

        # Test valid CIDv1 strings
        self.assertTrue(
            Validator(
                "bafybeie2reiz2q6rbcuwpy2etyztjnceolu4rdi7rp3th2lsky4r5ckeey"
            ).is_ipfs()
        )

        # Test invalid CIDv1 strings
        self.assertFalse(
            Validator(
                "bafybeie2reiz2q6rbcuwpy2etyztjnceolu4rdi7rp3th2lsky4r5ckee"
            ).is_ipfs()
        )

        # Test invalid misc input
        self.assertFalse(Validator("").is_ipfs())
        self.assertFalse(Validator(1345).is_ipfs())

        self.assertTrue(
            Validator(
                cid.from_string("QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE7o")
            ).is_ipfs()
        )
        self.assertFalse(
            Validator(
                cid.CIDv0("QmYjtig7VQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE7o")
            ).is_ipfs()
        )
        self.assertFalse(Validator(cid.CIDv0("dfmqjdmfkjqdm")).is_ipfs())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
