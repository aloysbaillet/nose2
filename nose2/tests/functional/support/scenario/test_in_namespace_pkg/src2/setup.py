from setuptools import setup, find_packages


setup(name='rsub2',
      packages=find_packages(include='rootnamespace/sub2/*'),
      namespace_packages = ['rootnamespace'],
      zip_safe=True)
