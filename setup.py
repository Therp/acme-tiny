from setuptools import setup, find_packages

VERSION = '2.0.1'

DISTNAME = 'acme_tiny'
LICENSE = 'MIT'
MAINTAINER = "Daniel Roesler"
EMAIL = "None"
URL = "None"
DESCRIPTION = "None"
LONG_DESCRIPTION = "None"

setup(
    name=DISTNAME,
    version=VERSION,
    packages = find_packages(),
    license=LICENSE,
    url=URL,
    maintainer_email=EMAIL,
    maintainer=MAINTAINER,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION)
