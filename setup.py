#!/usr/bin/env python
import os
from setuptools import setup, find_packages


def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
        return f.read()


#def parse_requirements(filename):
#    """ load requirements from a pip requirements file """
#    lineiter = (line.strip() for line in open(filename))
#    return [line for line in lineiter if line and not line.startswith("#")]


#install_requires = parse_requirements('requirements.txt')

setup(
    name="kkt_colab_ssh",
    version="0.1",
    description='Create SSH tunel to a running colab notebook',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/lhGWTS/colab_ssh',
    author='kkt',
    author_email='kkt@gmail.com',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    keywords=['ssh', 'colab'],
    python_requires='>=3',
    py_modules=['ssh_colab'],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points="""
        [console_scripts]
        colab_ssh = colab_ssh:colab_ssh:main
        """
)
