from is_ipfs import Validator
import unittest
import tests.testing_data as testing_data


class TestCase(unittest.TestCase):
    def test_all(self):

        with self.subTest("Test valid CID entries from fixtures"):
            for key, value in testing_data.valid_entries["cid"].items():
                for entries in value:
                    self.assertTrue(Validator(entries).is_ipfs())

        with self.subTest("Test invalid CID entries from fixtures"):
            for key, value in testing_data.invalid_entries["cid"].items():
                for entries in value:
                    self.assertFalse(Validator(entries).is_ipfs())

        with self.subTest("Test valid IPFS URL entries from fixtures"):
            for key, value in testing_data.valid_entries["url"].items():
                for entries in value:
                    self.assertTrue(Validator(entries).is_ipfs())

        with self.subTest("Test invalid IPFS URL entries from fixtures"):
            for entry in testing_data.invalid_entries["url"]["ipfs"]:
                self.assertFalse(Validator(entry).is_ipfs())

        with self.subTest("Test valid IPFS subdomain entries from fixtures"):
            for entry in testing_data.valid_entries["subdomain"]["ipfs"]:
                self.assertTrue(Validator(entry).is_ipfs())

        with self.subTest("Test invalid IPFS subdomain entries from fixtures"):
            for entry in testing_data.invalid_entries["subdomain"]["ipfs"]:
                self.assertFalse(Validator(entry).is_ipfs())


if __name__ == "__main__":
    unittest.main()
