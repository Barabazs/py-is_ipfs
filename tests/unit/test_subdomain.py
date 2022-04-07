from is_ipfs import Validator
import unittest
import tests.testing_data as testing_data


class TestCase(unittest.TestCase):
    def test_ipfs_subdomain(self):
        with self.subTest("Test valid IPFS subdomain entries from fixtures"):
            for entry in testing_data.valid_entries["subdomain"]["ipfs"]:
                self.assertTrue(Validator(entry)._ipfs_subdomain_url())

        with self.subTest("Test invalid IPFS subdomain entries from fixtures"):
            for entry in testing_data.invalid_entries["subdomain"]["ipfs"]:
                self.assertFalse(Validator(entry)._ipfs_subdomain_url())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
