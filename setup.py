import pathlib

import setuptools

long_description = pathlib.Path("README.md").read_text()

setuptools.setup(
    name="znjson",
    version="0.1.2",
    author="zincwarecode",
    author_email="zincwarecode@gmail.com",
    description="A Python Package to Encode/Decode some common file formats to json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zincware/ZnJSON",
    download_url="https://github.com/zincware/ZnJSON/archive/beta.tar.gz",
    keywords=["json", "zntrack", "jsonpickle", "serialization", "deserialization"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
)
