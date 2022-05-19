import unittest

from is_ipfs import Validator
from tests import testing_data


class TestCase(unittest.TestCase):
    def test_native_url(self):
        with self.subTest("Test valid IPFS native URL entries from fixtures"):
            for entry in testing_data.valid_entries["native_url"]["ipfs"]:
                self.assertTrue(Validator(entry)._is_native_ipfs_url())

        with self.subTest("Test invalid IPFS native URL entries from fixtures"):
            for entry in testing_data.invalid_entries["native_url"]["ipfs"]:
                self.assertFalse(Validator(entry)._is_native_ipfs_url())

        with self.subTest("Test valid IPNS native URL entries from fixtures"):
            for entry in testing_data.valid_entries["native_url"]["ipns"]:
                self.assertTrue(Validator(entry)._is_native_ipns_url())

        with self.subTest("Test invalid IPNS native URL from fixtures"):
            for entry in testing_data.invalid_entries["native_url"]["ipns"]:
                self.assertFalse(Validator(entry)._is_native_ipns_url())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
