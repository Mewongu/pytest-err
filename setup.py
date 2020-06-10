# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg


from setuptools import setup, find_packages


import pytest_err

setup(
    name="pytest-err",
    version=pytest_err.__version__,
    description="Error reporting plugin for pytest",
    long_description="""\
Gathers information about errors in tests provides information on similarity in root causes.
""",
    keywords="pytest error report",
    packages=find_packages(),
    include_package_data=True,
    entry_points={"pytest11": ["err = pytest_err.plugin"]},
    author="Andreas Stenberg",
    author_email="andreas@mewongu.com",
    url="https://github.com/Mewongu/pytest_err",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Software Development :: Testing",
    ],
)
