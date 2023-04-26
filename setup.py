from setuptools import setup, find_packages
import codecs
import os

#To create package: python setup.py sdist bdist_wheel
#To upload package: twine upload dist/*

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '2.1.0'
DESCRIPTION = 'This script will set all movies and shows in your local Plex library to English non forced subtitles by default.'
LONG_DESCRIPTION = 'This python script will set all movies and shows in your local Plex library to English non forced subtitles by default. The subtitle selections will apply to your Plex profile and be remembered on other devices.'

# Setting up
setup(
    name="PlexPreferNonForcedSubs",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/RileyXX/PlexPreferNonForcedSubs",
    packages=find_packages(),
    install_requires=['plexapi'],
    keywords=['python', 'video', 'plex', 'subtitles', 'subs'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'PlexPreferNonForcedSubs = PlexPreferNonForcedSubs.PlexPreferNonForcedSubs:main'
        ]
    }
)