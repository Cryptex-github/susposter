import re
from setuptools import setup
from setuptools_rust import Binding, RustExtension, Strip

setup_requires = ['setuptools-rust>=0.9.2']
install_requires = []

setup(name='susposter',
      author="Cryptex",
      version=version,
      description="so sussy",
      long_description="sussy imposter,
      url="https://github.com/Cryptex-github/susposter",
      rust_extensions=[
          RustExtension('susposter.susposter', 'Cargo.toml', binding=Binding.PyO3, strip=Strip.Debug)],
      setup_requires=setup_requires,
      include_package_data=True,
      packages=['susposter'],
      zip_safe=False,
      python_requires='>=3.6'
      )
