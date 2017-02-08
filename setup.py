"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name='Sortowanie',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description='Implementacje algorytmow sortowania',



    # Author details
    author='Lukasz Smoluch, Jacek Wierucki',
    author_email='smoluchlukasz@gmail.com',

    # Choose your license
    license='open-source',


    classifiers=[
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5'
    ],


    keywords='sorting bubble sort quicksort insert',

    packages=find_packages(exclude=['__init__', 'my_sort']),

    py_modules=['my_sort'],

    install_requires=['my_sort'],

    package_data={
        'sortowanie': ['__init__', 'my_sort'],
    },

    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)