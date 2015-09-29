from setuptools import setup, find_packages
from codecs import open
from os import path

from csvtojson import get_version


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-csvtojson',
    version=get_version(),
    description='Convert a csv file into a json file for django migrations.',
    long_description=long_description,
    url='https://github.com/njamaleddine/django-csvtojson',
    author='Nabil Jamaleddine',
    # Please send all proper requests through github issues
    author_email='njamaleddine@users.noreply.github.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='django migrations database development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    package_data={
        'sample': ['package_data.dat'],
    },
    entry_points={
        'console_scripts': [
            'django_csvtojson=django_csvtojson:main',
        ],
    },
)
