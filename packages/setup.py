
import io
import os
from pathlib import Path

from setuptools import setup

# Package Metadata
NAME = "regression_model"
DESCRIPTION = "Train and deploy regression model"
URL = "Abboah's github project"
EMAIL = "abboahbaah@gmail.com"
AUTHOR = "Bernard Baah Abboah"
REQUIRES_PYTHON = ">=3.6.0"

# What packages are required for this model to be executed?

def list_reqs(fname= "requirements.txt"):
    with open(fname) as fd:
        return fd.read().splitlines()


# The rest you shouldn't have to touch too much
here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: This will only work if "README" is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION



# Load the package's __version__.py module as a dictionary.

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / "regression_model"
CONFIG_DIR = PACKAGE_DIR / "Config"
VERSION_DIR = CONFIG_DIR / NAME
about = {}
with open(CONFIG_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version



# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    package_data={"regression_model": ["VERSION"]},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license="Capable African",
    Classifiers=[
        #Trove classifiers
        "Programming Language : : Python" 
    ]


)
