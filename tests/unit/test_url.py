import unittest

from is_ipfs import Validator
from tests import testing_data


class TestCase(unittest.TestCase):
    def test_ipfs_url(self):
        with self.subTest("Test valid IPFS URL entries from fixtures"):
            for entry in testing_data.valid_entries["url"]["ipfs"]:
                self.assertTrue(Validator(entry)._is_ipfs_url(), entry)

        with self.subTest("Test invalid IPFS URL entries from fixtures"):
            for entry in testing_data.invalid_entries["url"]["ipfs"]:
                self.assertFalse(Validator(entry)._is_ipfs_url(), entry)

        with self.subTest("Test valid IPNS URL entries from fixtures"):
            for entry in testing_data.valid_entries["url"]["ipns"]:
                self.assertTrue(Validator(entry)._is_ipns_url(), entry)

        with self.subTest("Test invalid IPNS URL entries from fixtures"):
            for entry in testing_data.invalid_entries["url"]["ipns"]:
                self.assertFalse(Validator(entry)._is_ipns_url(), entry)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
