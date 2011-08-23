# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

classifiers = """\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
License :: OSI Approved :: Zope Public License
Programming Language :: Python
Programming Language :: SQL
Topic :: Database
Topic :: Database :: Front-Ends
Topic :: Software Development
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: Microsoft :: Windows
Operating System :: Unix
"""

setup(name='Products.ZPsycopgDA',
      version='2.0.13-enfold',
      description='Python-PostgreSQL Zope Database Adapter.',
      classifiers=filter(None, classifiers.split("\n")),
      maintainer="Federico Di Gregorio",
      maintainer_email="fog@initd.org",
      author="Federico Di Gregorio",
      author_email="fog@initd.org",
      url="http://initd.org/tracker/psycopg",
      download_url = "http://initd.org/pub/software/psycopg2",
      license="GPL with exceptions or ZPL",
      platforms = ["any"],
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'psycopg2',
          'Products.ZSQLMethods'
      ],
      )
