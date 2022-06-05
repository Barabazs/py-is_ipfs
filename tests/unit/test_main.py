import subprocess
import unittest

from tests import testing_data


class TestCase(unittest.TestCase):
    def test_no_arguments(self):
        result = subprocess.run(["python3", "is_ipfs"], capture_output=True)
        self.assertIn(
            "is_ipfs: error: the following arguments are required: input",
            str(result.stderr),
        )

    def test_help(self):
        result = subprocess.run(["python3", "is_ipfs", "--help"], capture_output=True)
        self.assertIn("usage: is_ipfs [-h] input", str(result.stdout))
        self.assertIn(
            "Check if a string is a valid IPFS resource/object.", str(result.stdout)
        )
        self.assertIn("The string you want to validate", str(result.stdout))

    def test_valid_input(self):
        with self.subTest("Valid input"):
            categories = ["cid", "url", "subdomain", "path", "native_url"]
            for category in categories:
                for dict_value in testing_data.valid_entries[category].values():
                    for value in dict_value:
                        if isinstance(value, str):
                            result = subprocess.run(
                                ["python3", "is_ipfs", value], capture_output=True
                            )
                            self.assertIn("True", str(result.stdout))

        with self.subTest("Invalid input"):
            categories = ["cid", "url", "subdomain", "path", "native_url"]
            for category in categories:
                for dict_value in testing_data.invalid_entries[category].values():
                    for value in dict_value:
                        if isinstance(value, str):
                            result = subprocess.run(
                                ["python3", "is_ipfs", value], capture_output=True
                            )
                            self.assertIn("False", str(result.stdout))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
