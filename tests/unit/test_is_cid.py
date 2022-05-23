import unittest

from is_ipfs import Validator
from tests import testing_data


class TestCase(unittest.TestCase):
    def test_is_cid(self):
        with self.subTest("Test valid CID entries from testing data"):
            for value in testing_data.valid_entries["cid"].values():
                for entry in value:
                    self.assertTrue(Validator(entry)._is_cid(), entry)

        with self.subTest("Test invalid CID entries from testing data"):
            for value in testing_data.invalid_entries["cid"].values():
                for entry in value:
                    self.assertFalse(Validator(entry)._is_cid(), entry)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
