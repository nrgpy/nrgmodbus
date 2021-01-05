from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='nrgmodbus',
    version='0.3.1',
    description='library for making modbus connections to NRG Systems devices.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nrgpy/nrgmodbus',
    author='NRG Systems, Inc.',
    author_email='support@nrgsystems.com',
    licence='MIT',
    keywords='nrg systems symphoniepro ipackaccess wind modbus spidar',
    packages=find_packages(),
    install_requires=[
        'pymodbus',
        'requests',
    ],
    python_requires='>=3.0',
    zip_safe=True,
    include_package_data=True,
)
