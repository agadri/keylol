from setuptools import setup

APP = ['keylogger.py']
DATA_FILES = []
OPTIONS = {'packages': ['pynput']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)