import unittest

import tests.testing_data as testing_data
from is_ipfs import Validator


class TestCase(unittest.TestCase):
    def tests_is_ipfs_path(self):
        with self.subTest("Test valid IPFS path entries from fixtures"):
            for entry in testing_data.valid_entries["path"]["ipfs"]:
                self.assertTrue(Validator(entry)._is_ipfs_path())

        with self.subTest("Test invalid IPFS path entries from fixtures"):
            for entry in testing_data.invalid_entries["path"]["ipfs"]:
                self.assertFalse(Validator(entry)._is_ipfs_path())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
