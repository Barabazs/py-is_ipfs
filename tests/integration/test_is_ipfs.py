import unittest

import tests.testing_data as testing_data
from is_ipfs import Validator


class TestCase(unittest.TestCase):
    def test_all(self):

        with self.subTest("Test valid CID entries from fixtures"):
            for key, value in testing_data.valid_entries["cid"].items():
                for entry in value:
                    self.assertTrue(Validator(entry).is_ipfs())

        with self.subTest("Test invalid CID entries from fixtures"):
            for key, value in testing_data.invalid_entries["cid"].items():
                for entry in value:
                    self.assertFalse(Validator(entry).is_ipfs())

        with self.subTest("Test valid IPFS URL entries from fixtures"):
            for entry in testing_data.valid_entries["url"]["ipfs"]:
                self.assertTrue(Validator(entry).is_ipfs())

        with self.subTest("Test invalid IPFS URL entries from fixtures"):
            for entry in testing_data.invalid_entries["url"]["ipfs"]:
                self.assertFalse(Validator(entry).is_ipfs())

        with self.subTest("Test valid IPFS subdomain entries from fixtures"):
            for entry in testing_data.valid_entries["subdomain"]["ipfs"]:
                self.assertTrue(Validator(entry).is_ipfs())

        with self.subTest("Test invalid IPFS subdomain entries from fixtures"):
            for entry in testing_data.invalid_entries["subdomain"]["ipfs"]:
                self.assertFalse(Validator(entry).is_ipfs())

        with self.subTest("Test valid IPFS path entries from fixtures"):
            for entry in testing_data.valid_entries["path"]["ipfs"]:
                self.assertTrue(Validator(entry).is_ipfs())

        with self.subTest("Test invalid IPFS path entries from fixtures"):
            for entry in testing_data.invalid_entries["path"]["ipfs"]:
                self.assertFalse(Validator(entry).is_ipfs())

        with self.subTest("Test valid IPNS URL entries from fixtures"):
            for entry in testing_data.valid_entries["url"]["ipns"]:
                self.assertTrue(Validator(entry).is_ipfs())

        with self.subTest("Test invalid IPNS URL entries from fixtures"):
            for entry in testing_data.invalid_entries["url"]["ipns"]:
                self.assertFalse(Validator(entry).is_ipfs())

        with self.subTest("Test valid IPNS subdomain entries from fixtures"):
            for entry in testing_data.valid_entries["subdomain"]["ipns"]:
                self.assertTrue(Validator(entry).is_ipfs())

        with self.subTest("Test invalid IPNS subdomain entries from fixtures"):
            for entry in testing_data.invalid_entries["subdomain"]["ipns"]:
                self.assertFalse(Validator(entry).is_ipfs())

        with self.subTest("Test valid IPNS path entries from fixtures"):
            for entry in testing_data.valid_entries["path"]["ipns"]:
                self.assertTrue(Validator(entry).is_ipfs())

        with self.subTest("Test invalid IPNS path entries from fixtures"):
            for entry in testing_data.invalid_entries["path"]["ipns"]:
                self.assertFalse(Validator(entry).is_ipfs())


if __name__ == "__main__":
    unittest.main()
