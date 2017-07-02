from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

packages = ['validate']
setup(
    name='vlde',
    version='0.0.1',
    description='A data integrity check library',
    long_description=readme,
    author='Luo Xiaojie',
    author_email='xiaojieluoff@gmail.com',
    url='https://github.com/xiaojieluo/validate',
    license=license,
    packages=packages,
    # test_suite='tests'
)
