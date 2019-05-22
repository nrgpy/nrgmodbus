from setuptools import setup


setup(
    name='nrgmodbus',
    version='0.1.2',
    packages=[
        'nrgmodbus',
    ],
    install_requires= [
        'pymodbus',
        'requests',
    ],
    python_requires='>=3.0',
)
