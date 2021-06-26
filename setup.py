#!/usr/bin/env python3
from setuptools import setup

setup(
    name="aiohttp-oauthlib",
    description="oauthlib for aiohttp clients.",
    author="Hugo Osvaldo Barrera",
    author_email="hugo@barrera.io",
    url="https://git.sr.ht/~whynothugo/aiohttp-oauthlib",
    license="ISC",
    py_modules=["aiohttp_oauthlib"],
    install_requires=[
        "oauthlib",
        "aiohttp",
    ],
    long_description=open("README.rst").read(),
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
