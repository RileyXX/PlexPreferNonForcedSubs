# PlexPreferNonForcedSubs

## Short Description
This Python script sets all movies and shows in your local Plex library to English non-forced subtitles by default. It is compatible with Python 3.5 or later and designed to work on any operating system where Python is installed (Windows, macOS, Linux, etc).

## Long Description
This script utilizes the Plex Python API and sets all movies and shows in your local Plex library to English non-forced subtitles by default. The subtitle preferences will be applied to your Plex profile and remembered on other devices. By default, Plex prefers forced subtitles when available for a given item. However, Plex does not natively allow you to prefer non-forced subtitles, which is why this script was created.

The script has been thoroughly tested and confirmed to be working. Feel free to use the code for your own purposes. I will be running this code periodically on my home server along with some other Plex scripts, such as [Plex Auto Delete](https://github.com/Casvt/Plex-scripts/blob/main/changing_settings/plex_auto_delete.py). Special thanks to everyone who provided assistance! If you encounter any bugs while using this script, please open an issue. Cheers!

## What are "non-forced" subtitles?
Non-forced subtitles provide subtitles everytime a characters speaks.

## What are "forced" subtitles?
Forced subtitles only provide subtitles when the characters speak a foreign or alien language.

## Installation Instructions
1. Install [Python](https://www.python.org/downloads/) (v3.5 or later).
2. Install the script by executing the following in the command line: `python -m pip install PlexPreferNonForcedSubs`.
3. Ensure that your Plex media server is running, then run the script using `PlexPreferNonForcedSubs` in the command line.
4. On the first run, the script will prompt you to enter your [Plex token](https://www.plexopedia.com/plex-media-server/general/plex-token/). The token will be saved locally in the same folder as `token.txt`.
5. Done, setup complete. The script will continue to run and set all movies and shows in your local Plex library to use English non-forced subtitles.

See the section below for instructions on how to run, update, and uninstall the script.

## Installing the Script:
```
python -m pip install PlexPreferNonForcedSubs
```
_Execute in your operating system's native command line._
## Running the Script:
```
PlexPreferNonForcedSubs
```
_Execute in your operating system's native command line._
## Updating the Script:
```
python -m pip install PlexPreferNonForcedSubs --upgrade
```
_Execute in your operating system's native command line._
## Uninstalling the Script:
```
python -m pip uninstall PlexPreferNonForcedSubs
```
_Execute in your operating system's native command line._

## Installing a Specific Version:
```
python -m pip install PlexPreferNonForcedSubs==VERSION_NUMBER
```
_Replace `VERSION_NUMBER` with your [desired version](https://github.com/RileyXX/PlexPreferNonForcedSubs/releases) (e.g. 2.1.4) and execute in your operating system's native command line._

## Alternative Manual Installation Method (without pip install):
1. Install [Python](https://www.python.org/downloads/) (v3.5 or later).
2. Download the latest `.py` script from the [releases page](https://github.com/RileyXX/PlexPreferNonForcedSubs/releases) and move it to the desired directory.
3. Execute the script by running `PlexPreferNonForcedSubs.py`, or open the terminal and navigate to the folder where `PlexPreferNonForcedSubs.py` is located, then run `PlexPreferNonForcedSubs.py` in the terminal.
4. On the first run, the script will prompt you to enter your [Plex token](https://www.plexopedia.com/plex-media-server/general/plex-token/). The token will be saved locally in the same folder as `token.txt`.
5. Done.

See the section above for instructions on how to run, update, and uninstall the script.

## Known Issues/Future Outlook
- Some lines of redundant code can be shortened and/or removed. Refer to [this issue](https://github.com/RileyXX/PlexPreferNonForcedSubs/issues/4) for more details.

## Also Posted On
- [PyPi](https://pypi.org/project/PlexPreferNonForcedSubs/)
- [Reddit](https://www.reddit.com/r/PleX/comments/105gdh7/python_code_to_set_all_movies_and_shows_in_plex/)
- [Stack Overflow](https://stackoverflow.com/q/75027919/9196825)
- [Plex Forums](https://forums.plex.tv/t/python-script-to-set-all-movies-and-shows-in-plex-to-use-english-non-forced-subtitles/825871)

## Screenshots:
##### Plex subtitle dropdown after script is done running:
![Plex Subtitle Dropdown](https://i.imgur.com/BNOlwtL.png)
##### PlexPreferNonForcedSubs.py script in action:
![PlexPreferNonForcedSubs.py Script in Action](https://github.com/RileyXX/PlexPreferNonForcedSubs/raw/main/demo.gif)

## Sponsorships, Donations, and Custom Projects
If you find my scripts helpful, you can become a [sponsor](https://github.com/sponsors/RileyXX) and support my projects! If you need help with a project, open an issue, and I'll do my best to assist you. For other inquiries and custom projects, you can contact me on [Twitter](https://twitter.com/RileyxBell).

#### More Donation Options:
- Cashapp: `$rileyxx`
- Venmo: `@rileyxx`
- Bitcoin: `bc1qrjevwqv49z8y77len3azqfghxrjmrjvhy5zqau`
- Amazon Wishlist: [Link ↗](https://www.amazon.com/hz/wishlist/ls/WURF5NWZ843U)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
