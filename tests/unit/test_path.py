import unittest

from is_ipfs import Validator
from tests import testing_data


class TestCase(unittest.TestCase):
    def tests_is_ipfs_path(self):
        with self.subTest("Test valid IPFS path entries from fixtures"):
            for entry in testing_data.valid_entries["path"]["ipfs"]:
                self.assertTrue(Validator(entry)._is_ipfs_path())

        with self.subTest("Test invalid IPFS path entries from fixtures"):
            for entry in testing_data.invalid_entries["path"]["ipfs"]:
                self.assertFalse(Validator(entry)._is_ipfs_path())

        with self.subTest("Test valid IPNS path entries from fixtures"):
            for entry in testing_data.valid_entries["path"]["ipns"]:
                self.assertTrue(Validator(entry)._is_ipns_path())

        with self.subTest("Test invalid IPNS path entries from fixtures"):
            for entry in testing_data.invalid_entries["path"]["ipns"]:
                self.assertFalse(Validator(entry)._is_ipns_path())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
