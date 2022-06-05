import argparse
import sys

from is_ipfs import Validator


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check if a string is a valid IPFS resource/object.", prog="is_ipfs"
    )

    parser.add_argument("input", type=str, help="The string you want to validate")

    args = parser.parse_args()

    print(Validator(args.input).is_ipfs())


if __name__ == "__main__":
    sys.exit(main(sys.argv))
