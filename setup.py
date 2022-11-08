from setuptools import setup

setup(
    name='dexpy',
    version='0.1.0',
    description='Differential Expression Analysis in Python',
    author='Ian R. Dinsmore',
    author_email='iandinsmore1@gmail.com',
    url='https://github.com/idinsmore1/dexpy',
    packages=['dexpy'],
    install_requires=[
        'numpy',
        'pandas',
        'numba',
        ],
)