from os import path

from setuptools import setup, find_packages

# The directory containing this file
PATH = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(PATH, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read the requirements file
with open(path.join(PATH, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().splitlines()

# Read the __version__ variable from rclone_manager/__version__.py
about = {}
with open(path.join(PATH, 'rclone_manager', '__version__.py'), encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    license=about['__license__'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='rclone manager sync copy move file',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=requirements,
    python_requires='>=3.8',
)
