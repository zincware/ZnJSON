import setuptools
import pathlib

long_description = pathlib.Path("README.md").read_text()

setuptools.setup(
    name="znconv",
    version="0.0.2",
    author="zincwarecode",
    author_email="zincwarecode@gmail.com",
    description="A Python Package to Encode/Decode some common file formats to json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zincware/ZnConv",
    download_url="https://github.com/zincware/ZnConv/archive/beta.tar.gz",
    keywords=["json", "zntrack"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
)
