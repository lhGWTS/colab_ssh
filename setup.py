
#!/usr/bin/env python
import os
from setuptools import setup, find_packages


#def parse_requirements(filename):
#    """ load requirements from a pip requirements file """
#    lineiter = (line.strip() for line in open(filename))
#    return [line for line in lineiter if line and not line.startswith("#")]


#install_requires = parse_requirements('requirements.txt')

setup(
    name="kkt_colab_ssh",
    version="0.1",
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    keywords=['ssh', 'colab'],
    python_requires='>=3',
    py_modules=['colab_ssh'],
    entry_points="""
        [console_scripts]
        colab_ssh = colab_ssh:main
        """
)
