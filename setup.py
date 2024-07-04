from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup (
    name="ws-core",
    version="0.1",
    author="Nick Rodriguez",
    author_email="nrodrig1@gmail.com",
    description="ws stands for What Sticks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/costa-rica/WhatSticks13Core",
    packages=['ws_config', 'ws_models'],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
