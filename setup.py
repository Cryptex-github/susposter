import re
from setuptools import setup

with open('susposter/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(name='susposter',
      author="Cryptex",
      version=version
      description="so sussy",
      long_description=open("README.md").read()
      url="https://github.com/Cryptex-github/susposter",
      include_package_data=True,
      packages=['susposter'],
      zip_safe=True,
      python_requires='>=3.6'
      )
