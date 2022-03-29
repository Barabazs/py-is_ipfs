# py-is_ipfs
[![Latest release](https://img.shields.io/pypi/v/py-is_ipfs?color=blue&label=release)](https://github.com/Barabazs/py-is_ipfs/releases/latest)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Barabazs/py-is_ipfs/Test?label=Test&logo=github)

py-is_ipfs is a Python library to identify valid IPFS resources.  
This project is a work in progress.

## Installation and usage
### Installation
py-is_ipfs is available on PyPI:

`python -m pip install py_is-ipfs`

### Usage

```python
from is_ipfs import Validator

print(Validator("QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE7o").is_ipfs())
```
## Currently supported
* [x] CID
  * [x] v0
  * [x] v1
* [ ] URL
  * [ ] IPFS
  * [ ] IPNS
* [ ] Subdomain
  * [ ] IPFS
  * [ ] IPNS
* [ ] Path
* [ ] ...

## License
[MIT](https://github.com/Barabazs/py-is_ipfs/blob/main/LICENSE)
