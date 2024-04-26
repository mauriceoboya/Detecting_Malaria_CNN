import setuptools 
import os

with open("README.md",'r',encoding="utf-8") as file:
    long_description=file.read()

REPO_NAME='Detecting_Malaria_CNN'
SRC_REPO=f"malaria_cnn"
AUTHOR_NAME='mauriceoboya'
__version__="0.1.0"
AUTHOR_EMAIL="mauriq97@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    package_dir={'':"src"},
    packages=setuptools.find_packages(where='src')

)