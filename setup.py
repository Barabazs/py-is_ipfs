import setuptools

setuptools.setup(
    name="is_ipfs",
    version="0.0.0",
    description="Python library to identify valid IPFS resources",
    url="https://github.com/Barabazs/py-is_ipfs",
    author="Barabazs",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
