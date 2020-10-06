import setuptools

# with open("README.md", "r") as fh:
#     LONG_DESCRIPTION = fh.read()

# LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

NAME = "vae-wae"
DESCRIPTION = "WAE"
URL = "https://github.com/locus-taxy/wae"
REQUIRES_PYTHON = ">=3.7"

with open("wae/version.txt") as version_file:
    VERSION = version_file.read()

AUTHOR = "Abhishek Roy"
AUTHOR_EMAIL = "abhishekr@locus.sh"

REQUIRED = [
    "dateparser == 0.7.2",
    "dpath == 1.4.2",
    "numpy == 1.18.1",
    "pandas == 1.0.1",
    "scipy == 1.4.1",
    "tsplib95 == 0.7.0",
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    url=URL,
    packages=setuptools.find_packages(exclude=["wae_api", "wae_api.*"]),
    package_data={
        "": ["*.ini", "*.txt"]
    },
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    entry_points={
        "console_scripts": ["vae-wae=wae.run:main"]
    },
)