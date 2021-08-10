from setuptools import setup
from pkg_resources import parse_version
import re

def GetVersion():
    with open('geodesic/__init__.py') as f:
        return parse_version(re.findall(r'__version__\s*=\s*\'([.\d]+-*[a-z]*[.\d]*)\'', f.read())[0])

setup(
    name='test_package',
    version=GetVersion(),
    license='Apache-2.0',
    description='A test for publishing from github actions',
    url='http://seerai.space',
    author='Me',
    packages=["test_package"]
)