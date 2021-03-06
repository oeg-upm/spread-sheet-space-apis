import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

description = """"""

# The text of the README file
with open("README.md") as f:
    README = f.read()
    lines = README.split('\n')
    desc_lines = [line for line in lines if line[:2] != "[!"]
    README = "\n".join(desc_lines)
# This call to setup() does all the work
setup(
    name="spreadsheet-space-apis",
    version="1.0.1",
    description=description,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/oeg-upm/spread-sheet-space-apis",
    author="Ahmad Alobaid",
    author_email="aalobaid@fi.upm.es",
    license="Apache2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["spreadsheetspace"],
    include_package_data=True,
    install_requires=["requests", "pandas"]
)
