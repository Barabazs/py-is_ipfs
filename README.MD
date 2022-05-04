# py-is_ipfs
[![Latest release](https://img.shields.io/pypi/v/py-is_ipfs?color=blue&label=release)](https://github.com/Barabazs/py-is_ipfs/releases/latest) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Barabazs/py-is_ipfs/Test?label=Test&logo=github)

py-is_ipfs is a Python library to identify valid IPFS resources.  
This project is a work in progress.

## Installation and usage
### Installation
py-is_ipfs is available on PyPI:

`python -m pip install py-is_ipfs`

### Usage

```python
from is_ipfs import Validator

print(Validator("QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE7o").is_ipfs())
```
## Currently supported
* [x] CID
  * [x] v0
  * [x] v1
* [x] URL
  * [x] Path Gateway
    * [x] IPFS
    * [x] IPNS
  * [x] Subdomain Gateway
    * [x] IPFS
    * [x] IPNS
* [x] Path
  * [x] IPFS
  * [x] IPNS
* [ ] ...

## License
[MIT](https://github.com/Barabazs/py-is_ipfs/blob/main/LICENSE)

## Acknowledgments
* [Protocol Labs](https://protocol.ai/) for funding this project with a micro grant.
* [ipfs-shipyard/is-ipfs](https://github.com/ipfs-shipyard/is-ipfs) for the heuristics implemented in JavaScript that this project used as a starting point.
