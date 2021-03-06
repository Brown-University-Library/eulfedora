#!/usr/bin/env python

from setuptools import setup, find_packages
import sys
import eulfedora

LONG_DESCRIPTION = None
try:
    # read the description if it's there
    with open('README.rst') as desc_f:
        LONG_DESCRIPTION = desc_f.read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

requirements = [
    'ply==3.8',
    'eulxml>=1.1.3',
    'rdflib>=3.0',
    'python-dateutil',
    'requests>=2.21.0',
    'requests-toolbelt>=0.9.1',
    'pycrypto',
    'pypdf2',
    'six',
]

test_requirements = [
    'sphinx',
    'nose',
    'coverage',
    'mock',
    'pyPdf',
    'tox',
    'progressbar2'
]

dev_requirements = test_requirements + ['Django']

if sys.version_info < (3, 0):
    requirements.append('progressbar2')

setup(
    name='eulfedora',
    version=eulfedora.__version__,
    author='Emory University Libraries',
    author_email='libsysdev-l@listserv.cc.emory.edu',
    url='https://github.com/emory-libraries/eulfedora',
    license='Apache License, Version 2.0',
    packages=find_packages(),
    install_requires=requirements,
    # indexdata utils are optional. They include things like PDF text stripping (pyPdf).
    # Be sure to include the below in your own pip dependencies file if you need to use
    # the built in indexer utility support.
    extras_require={
        'indexdata_util': ['pypdf2'],
        'django': ['Django'],
        'dev': dev_requirements,
        'test': test_requirements,
    },
    description='Idiomatic access to digital objects in a Fedora Commons repository',
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    scripts=['scripts/fedora-checksums', 'scripts/validate-checksums',
             'scripts/repo-cp'],
    include_package_data=True,
    package_data={'eulfedora': ['eulfedora/templates/eulfedora/*.html']},
)
