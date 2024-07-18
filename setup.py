import setuptools

setuptools.setup(
    name="satellitescraper",
    version="0.1.0",
    author="Mostafa Mabrok",
    author_email="mostafa.m.mabrok@gmail.com",
    description="Python Package for Scraping Sattelite Image Data",
    long_description="PLACEHOLDER",
    long_description_content_type="text/markdown",
    url="https://github.com/Mostafamabrok/longitude",
    install_requires=['certifi==2020.12.5','chardet==4.0.0','chromedriver-autoinstaller==0.2.2','idna==2.10',
                      'numpy==1.19.5','requests==2.25.1','selenium==4.10.0','tqdm==4.53.0','urllib3==1.26.5', 
                      'opencv-python==4.5.5.64'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

