# PlexPreferNonForcedSubs


## Short description:
This python script will set all movies and shows in your local Plex library to English non forced subtitles by default. The subtitle selections will apply to your Plex profile and be remembered on other devices.

## Long description:
This script was created with the help of [ChatGPT Open AI](https://chat.openai.com/chat) and further edited and completed by me. It uses [Plex Python Api](https://python-plexapi.readthedocs.io/en/latest/). It will set all movies and shows in your local Plex library to English non forced subtitles by default. The subtitle selections will apply to your Plex profile and be remembered on other devices. Assuming your Plex subtitles settings are setup in your server settings Plex will default to Forced Subtitles by default when they are available for a given item. Plex will not allow you to prefer non forced subtitles natively hence why this script was created.

This script is confirmed tested and working. Feel free to use this code for your own purposes. I will be running this code periodically on my home server along with some of my other neat little plex scripts like [Plex Auto Delete](https://github.com/Casvt/Plex-scripts/blob/main/changing_settings/plex_auto_delete.py). Thanks to [all](https://stackoverflow.com/questions/75027919/python-script-to-set-all-subtitles-for-movies-shows-in-plex-to-english-non-for) who helped! If you use this script and run into any bugs feel free to open an issue. Cheers!

## What are "non-forced" subtitles?
Non-forced subtitles provide subtitles everytime a characters speaks.

## What are "forced" subtitles?
Forced subtitles only provide subtitles when the characters speak a foreign or alien language.


## Instructions:
1. Install [Python](https://www.python.org/downloads/).
2. Download the latest .py script from the [releases](https://github.com/RileyXX/PlexDefaultSubtitleChanger/releases) page. 
3. Replace `xxxxxxx` in the script with your [plex api token](https://www.plexopedia.com/plex-media-server/general/plex-token/).
4. Install python dependency [plexapi](https://github.com/pkkid/python-plexapi). To do this, run `python -m pip install plexapi` in command prompt.
5. Make sure Plex media server is running locally then run the script and watch it work its magic.

_Note: This script should work on any OS where Python is installed (Windows, MacOS and Linux etc)._

## Known issues/future outlook:
* Several lines of redundant code can be shortened and/or removed

## Also posted on:
* [Stackoverflow](https://stackoverflow.com/q/75027919/9196825)
* [Reddit](https://www.reddit.com/r/PleX/comments/105gdh7/python_code_to_set_all_movies_and_shows_in_plex/)
* [Plex Forums](https://forums.plex.tv/t/python-script-to-set-all-movies-and-shows-in-plex-to-use-english-non-forced-subtitles/825871)

## Screenshots:
##### Plex subtitle dropdown after script is done running:
![Plex Subtitle Dropdown](https://i.imgur.com/BNOlwtL.png)
##### PlexPreferNonForcedSubs.py script in action:
![PlexPreferNonForcedSubs.py Script in Action](https://github.com/RileyXX/PlexPreferNonForcedSubs/raw/main/demo.gif)

## Donations, Sponsorships and Custom Projects:
Like my scripts? Become a [sponsor](https://github.com/sponsors/RileyXX) and support my projects! See below for other donation options. Need help with a project? Open an issue and I will try my best to help! For other inquiries and custom projects contact me on [Twitter](https://twitter.com/RileyxBell).

#### More donation options:
- Cashapp: `$rileyxx`
- Venmo: `@rileyxx`
- Bitcoin: `bc1qrjevwqv49z8y77len3azqfghxrjmrjvhy5zqau`
- Amazon Wishlist: [Link ↗](https://www.amazon.com/hz/wishlist/ls/WURF5NWZ843U)

