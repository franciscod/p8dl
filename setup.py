from setuptools import setup

PACKAGE_NAME = 'p8dl'
GITHUB_BASE = 'https://github.com/franciscod/'
VERSION = '0.1'
setup(
    name=PACKAGE_NAME,
    packages=[PACKAGE_NAME],
    version=VERSION,
    description='PICO-8 cartridge downloader',
    author='Francisco Demartino',
    author_email='demartino.francisco@gmail.com',
    url=GITHUB_BASE + PACKAGE_NAME,
    download_url=GITHUB_BASE + PACKAGE_NAME + '/tarball/' + VERSION,
    keywords=['pico8', 'pico-8', 'lexaloffle'],
    classifiers=[],
    install_requires=[
        'appdirs',
    ],
    entry_points={
        'console_scripts': [
            'p8dl = p8dl.cli:main'],
    }
)
