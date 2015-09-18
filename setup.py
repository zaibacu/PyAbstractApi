#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup
from pip.req import parse_requirements

from pyabstractapi.version import get_version

install_reqs = list(parse_requirements("requirements", session={}))

setup(name="pyabstractapi",
		version=get_version(),
		description="A minimalistic framework for accessing restful APIs",
		author="Šarūnas Navickas",
		author_email="zaibacu@gmail.com",
		license="MIT",
		packages=["pyabstractapi"],
		install_requires=[str(ir.req) for ir in install_reqs],
		test_suite="nose.collector",
		tests_require=["nose"])