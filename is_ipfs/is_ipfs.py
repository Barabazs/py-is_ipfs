import re
import typing

import cid
from multibase import decode


class Validator:
    """
    Class for validating IPFS resources.
    """

    def __init__(self, input: typing.Any):
        self.input = input
        self.pathGatewayPattern = re.compile(
            r"^https?://[^/]+/(?P<protocol>ip[fn]s)/(?P<hash>[^/?#]+)"
        )
        self.subdomainGatewayPattern = re.compile(
            r"^https?://(?P<hash>[^/]+)\.(?P<protocol>ip[fn]s)\.[^/?]+"
        )

    def is_ipfs(self) -> bool:
        """
        Returns True if the provided input is a valid IPFS resource/object or False otherwise.
        """
        return self._is_CID() or self._is_ipfs_url()

    def _is_CID(self) -> bool:
        """
        Returns True if the provided string or CID object represents a valid CID or False otherwise.
        """
        if type(self.input) == str:
            return cid.is_cid(self.input)
        elif type(self.input) == bytes:
            try:
                return cid.is_cid(decode(self.input))
            except:
                return False
        else:
            try:
                if isinstance(self.input, (cid.CIDv0, cid.CIDv1)):
                    return cid.is_cid(str(self.input))
            except:
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

        if pattern == self.subdomainGatewayPattern:
            _hash = _hash.lower()

        return Validator(_hash)._is_CID()

    def _ipfs_subdomain_url(self) -> bool:
        """
        Returns True if the provided url string includes a valid IPFS subdomain (case-insensitive CIDv1) or False otherwise.
        """
        return self._is_integral_ipfs_url(
            self.subdomainGatewayPattern,
        )

    def _ipfs_path_url(self) -> bool:
        """
        Returns True if the provided url string is a valid IPFS URL or False otherwise.
        """

        return self._is_integral_ipfs_url(
            self.pathGatewayPattern,
        )
