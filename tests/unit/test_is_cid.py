import unittest

from is_ipfs import Validator
from tests import testing_data


class TestCase(unittest.TestCase):
    def test_is_cid(self):
        with self.subTest("Test valid CID entries from testing data"):
            for key, value in testing_data.valid_entries["cid"].items():
                for entry in value:
                    result = Validator(entry)._is_cid()
                    self.assertIsInstance(result, bool)
                    self.assertTrue(result)

        with self.subTest("Test invalid CID entries from testing data"):
            for key, value in testing_data.invalid_entries["cid"].items():
                for entry in value:
                    result = Validator(entry)._is_cid()
                    if result is None:
                        print(entry)
                    self.assertIsInstance(result, bool)
                    self.assertFalse(result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
