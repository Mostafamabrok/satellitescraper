import setuptools
import re
import ast

setuptools.setup(
    name="satellitescraper",
    version="0.1.2",
    author="Mostafa Mabrok",
    author_email="mostafa.m.mabrok@gmail.com",
    description="Python Package for Scraping Sattelite Image Data",
    long_description="PLACEHOLDER",
    long_description_content_type="text/markdown",
    url="https://github.com/Mostafamabrok/longitude",
    install_requires=['certifi','chardet','chromedriver-autoinstaller','idna',
                      'numpy','requests','selenium','tqdm','urllib', 
                      'opencv-python'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

