from setuptools import setup, find_packages

# This reads the __version__ variable from fermilibpluginpyscf/_version.py
exec(open('fermilibpluginpyscf/_version.py').read())
# Readme file as long_description:
long_description = open('README.rst').read()
# Read in requirements.txt
requirements = open('requirements.txt').readlines()
requirements = [r.strip() for r in requirements]


setup(
    name='fermilibpluginpyscf',
    version=__version__,
    author='FermiLib plugin PySCF developers',
    author_email='fermilib@projectq.ch',
    url='http://www.projectq.ch',
    description='A plugin allowing FermiLib to interface with PySCF.',
    long_description=long_description,
    install_requires=requirements,
    license='Apache 2',
    packages=find_packages()
)
