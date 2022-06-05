import setuptools

with open("README.MD") as f:
    long_description = f.read()


setuptools.setup(
    name="py-is_ipfs",
    version="0.4.0",
    description="Python library to identify valid IPFS resources",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Barabazs/py-is_ipfs",
    author="Barabazs",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=[
        "py-cid>=0.3.0<1.0.0",
        "py-multibase>=1.0.3,<2.0.0",
    ],
)
