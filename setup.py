import subprocess

import setuptools

_long_description = "See https://github.com/priv-kweihmann/tlv for documentation"
_long_description_content_type = "text/plain"
try:
    _long_description = subprocess.check_output(
        ["pandoc", "--from", "markdown", "--to", "rst", "README.md"]).decode("utf-8")
    _long_description_content_type = "text/x-rst"
except (subprocess.CalledProcessError, FileNotFoundError):
    pass

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="tlv",
    version="1.0.2",
    author="Konrad Weihmann",
    author_email="kweihmann@outlook.com",
    description="-- Too less variation -- Find duplicates in source code for various languages",
    long_description=_long_description,
    long_description_content_type=_long_description_content_type,
    url="https://github.com/priv-kweihmann/tlv",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    scripts=['bin/tlv'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
