from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Validate',
    version='0.0.1',
    description='A data integrity check library',
    long_description=readme,
    author='luoxiaojie',
    author_email='xiaojieluoff@gmail.com',
    url='https://github.com/xiaojieluo/validate',
    license=license,
    packages=find_packages(exclude('tests', 'docs'))
)
