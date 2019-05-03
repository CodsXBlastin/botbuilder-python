# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from setuptools import setup

REQUIRES = [
    "azure-cognitiveservices-language-luis==0.2.0",
    "botbuilder-schema>=4.0.0.a6",
    "botbuilder-core>=4.0.0.a6",
    "aiohttp>=3.5.4"
]

TESTS_REQUIRES = [
    "aiounittest>=1.1.0"
]

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, "botbuilder", "ai", "about.py")) as f:
    package_info = {}
    info = f.read()
    exec(info, package_info)

setup(
    name=package_info["__title__"],
    version=package_info["__version__"],
    url=package_info["__uri__"],
    author=package_info["__author__"],
    description=package_info["__description__"],
    keywords="botbuilder-ai LUIS QnAMaker bots ai botframework botbuilder",
    long_description=package_info["__summary__"],
    license=package_info["__license__"],
    packages=["botbuilder.ai", "botbuilder.ai.qna", "botbuilder.ai.luis"],
    install_requires=REQUIRES,
    tests_require=TESTS_REQUIRES,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ]
)