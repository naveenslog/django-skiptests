from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Django Library To Skip Tests'
LONG_DESCRIPTION = 'A Simple django library to skip some tests from a Django project.'

# Setting up
setup(
    name="django-skiptests",
    version=VERSION,
    author="Naveen Singh (Noida, India)",
    author_email="naveen.singh@outlook.in",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'django', 'skip tests', 'ignore tests', 'django ignore tests', 'django skip tests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)