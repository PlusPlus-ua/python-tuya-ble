#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["asyncio", "bleak", "bleak_retry_connector"]

test_requirements = []

setup(
    author="Oleksander Plias",
    author_email="alexplas@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Library to control Tuya BLE devices",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="tuya_ble",
    name="tuya_ble",
    packages=find_packages(include=["tuya_ble", "tuya_ble.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/PlusPlus-ua/tuya_ble",
    version="0.1.0",
    zip_safe=False,
)
