from .converters import (
    Base16StringConverter as Base16StringConverter,
    Base32StringConverter as Base32StringConverter,
    Base64StringConverter as Base64StringConverter,
    BaseStringConverter as BaseStringConverter,
    IdentityConverter as IdentityConverter,
)
from typing import List, NamedTuple, Union, Dict

class Encoding(NamedTuple):
    encoding: str
    code: bytes
    converter: Union[
        IdentityConverter,
        BaseStringConverter,
        Base16StringConverter,
        Base32StringConverter,
        Base64StringConverter,
    ]

CODE_LENGTH: int
ENCODINGS: List[Encoding]
ENCODINGS_LOOKUP: Dict[Union[str, bytes], Encoding]

def encode(encoding: str, data: Union[str, bytes]) -> bytes: ...
def get_codec(data: Union[str, bytes]) -> Encoding: ...
def is_encoded(data: Union[str, bytes]) -> bool: ...
def decode(data: Union[str, bytes]) -> str: ...
