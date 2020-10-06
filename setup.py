import setuptools

# with open("README.md", "r") as fh:
#     LONG_DESCRIPTION = fh.read()

# LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

NAME = "testSetupTools"
DESCRIPTION = "testing setup tools"
URL = "https://github.com/sagjounkani/testSetupTools"
REQUIRES_PYTHON = ">=3.6"

# with open("wae/version.txt") as version_file:
#     VERSION = version_file.read()

AUTHOR = "Sagar Jounkani"
AUTHOR_EMAIL = "sagjounkani@gmail.com"

REQUIRED = [
    "python-levenshtein == 0.12.0"
]

setuptools.setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=['testTools'],
    # package_data={
    #     "": ["*.ini", "*.txt"]
    # },
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    entry_points={
        "console_scripts": ["testTools=testTools.main:getData"]
    },
)