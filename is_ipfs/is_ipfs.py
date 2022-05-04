import re
import typing

import cid
from multibase import decode
from multibase import get_codec


class Validator:
    """
    Class for validating IPFS resources.
    """

    def __init__(self, input: typing.Any):
        self.input = input
        self.path_gateway_pattern = re.compile(
            r"^https?://[^/]+/(?P<protocol>ip[fn]s)/(?P<hash>[^/?#]+)"
        )
        self.subdomain_gateway_pattern = re.compile(
            r"^https?://(?P<hash>[^/]+)\.(?P<protocol>ip[fn]s)\.[^/?]+"
        )
        self.path_pattern = re.compile(r"^/(?P<protocol>ip[fn]s)/(?P<hash>[^/?#]+)")

    def is_ipfs(self) -> bool:
        """
        Returns True if the provided input is a valid IPFS resource/object or False otherwise.
        """
        return self._is_CID() or self._is_ipfs_url() or self._is_ipfs_path()

    def _is_CID(self) -> bool:
        """
        Returns True if the provided string or CID object represents a valid CID or False otherwise.
        """
        if type(self.input) == str:
            return cid.is_cid(self.input)
        elif type(self.input) == bytes:
            try:
                return cid.is_cid(decode(self.input))
            except Exception as error:
                print(f"Unexpected {type(error)}, {error}")
                return False
        else:
            try:
                if isinstance(self.input, (cid.CIDv0, cid.CIDv1)):
                    return cid.is_cid(str(self.input))
            except Exception as error:
                print(f"Unexpected {type(error)}, {error}")
                return False
        return False

    def _is_ipfs_url(self) -> bool:
        """
        Returns True if the provided string is a valid IPFS url or False otherwise.
        """
        return self._ipfs_path_url() or self._ipfs_subdomain_url()

    def _is_integral_ipfs_url(
        self,
        pattern: re.Pattern,
    ) -> bool:

        formatted = str(self.input)
        if not formatted:
            return False

        match = re.match(pattern, formatted)
        if not match:
            return False

        if match["protocol"] != "ipfs":
            return False

        _hash = match["hash"]

        if pattern == self.subdomain_gateway_pattern:
            _hash = _hash.lower()
            try:
                if get_codec(_hash).encoding not in ["base32", "base36"]:
                    return False
            except Exception as error:
                print(f"Unexpected {type(error)}, {error}")
                return False
        elif pattern == self.path_gateway_pattern:
            if not str(_hash).startswith("Qm"):
                try:
                    if get_codec(_hash).encoding not in [
                        "base2",
                        "base16",
                        "base32",
                        "base32hex",
                        "base36",
                        "base36upper",
                        "base58flickr",
                        "base58btc",
                        "base64url",
                        "base32",
                        "base36",
                    ]:
                        return False
                except Exception as error:
                    print(f"Unexpected {type(error)}, {error}")
                    return False

        return Validator(_hash)._is_CID()

    def _ipfs_subdomain_url(self) -> bool:
        """
        Returns True if the provided url string includes a valid IPFS subdomain (case-insensitive CIDv1) or False otherwise.
        """
        return self._is_integral_ipfs_url(
            self.subdomain_gateway_pattern,
        )

    def _ipfs_path_url(self) -> bool:
        """
        Returns True if the provided url string is a valid IPFS URL or False otherwise.
        """

        return self._is_integral_ipfs_url(
            self.path_gateway_pattern,
        )

    def _is_ipfs_path(self) -> bool:
        """
        Returns true if the provided string is a valid IPFS path or false otherwise.
        """
        return self._is_integral_ipfs_url(self.path_pattern)
