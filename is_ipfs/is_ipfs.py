import typing

import cid
from multibase import decode


class Validator:
    """
    Class for validating IPFS resources.
    """

    def __init__(self, input: typing.Any):
        self.input = input

    def is_ipfs(self) -> bool:
        """
        Returns True if the provided input is a valid IPFS CID or False otherwise.
        """
        return self._is_CID()

    def _is_CID(self) -> bool:
        """
        Returns true if the provided string or CID object represents a valid CID or false otherwise.
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
