import unittest

from is_ipfs import Validator
from tests import testing_data


class TestCase(unittest.TestCase):
    def test_ipfs_subdomain(self):
        with self.subTest("Test valid IPFS subdomain entries from fixtures"):
            for entry in testing_data.valid_entries["subdomain"]["ipfs"]:
                self.assertTrue(Validator(entry)._is_ipfs_subdomain_url(), entry)

        with self.subTest("Test invalid IPFS subdomain entries from fixtures"):
            for entry in testing_data.invalid_entries["subdomain"]["ipfs"]:
                self.assertFalse(Validator(entry)._is_ipfs_subdomain_url(), entry)

        with self.subTest("Test valid IPNS subdomain entries from fixtures"):
            for entry in testing_data.valid_entries["subdomain"]["ipns"]:
                self.assertTrue(Validator(entry)._is_ipns_subdomain_url(), entry)

        with self.subTest("Test invalid IPNS URL subdomain from fixtures"):
            for entry in testing_data.invalid_entries["subdomain"]["ipns"]:
                self.assertFalse(Validator(entry)._is_ipns_subdomain_url(), entry)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
