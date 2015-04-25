from setuptools import setup, find_packages


setup(name='rsub1',
      packages=find_packages(include='rootnamespace/sub1/*'),
      namespace_packages = ['rootnamespace'],
      zip_safe=True)
