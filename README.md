ccccc# PlexPreferNonForcedSubs


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
##### Windows:
To use this script on Windows. Simply install latest version of [Python](https://www.python.org/downloads/). 
1. Download the latest .py script from the [releases](https://github.com/RileyXX/PlexDefaultSubtitleChanger/releases) page. 
2. Replace xxxxxxx in the script with your [plex api token](https://www.plexopedia.com/plex-media-server/general/plex-token/).
3. Make sure Plex media server is running locally then run the script and watch it work its magic.

##### Note:
This script should work fine on any other operating system. No need to make any changes.

## Known issues/future outlook:
* Forced subs without the "forced" tag will be treated as non forced subs. This could be fixed in the script by checking the subtitle "title" tag for some variation of the word "forced". 
* [Python-PlexAPI](https://python-plexapi.readthedocs.io/en/latest/modules/media.html#plexapi.media.MediaPart.setDefaultSubtitleStream) has a method to set the default subtitle stream. No need to manually call the API using requests. 
* Several lines of redundant code can be shortened and/or removed
* Plans to print out neat colored data tables when the script runs

## Also posted on:
* [Stackoverflow](https://stackoverflow.com/q/75027919/9196825)
* [Reddit](https://www.reddit.com/r/PleX/comments/105gdh7/python_code_to_set_all_movies_and_shows_in_plex/)
* [Plex Forums](https://forums.plex.tv/t/python-script-to-set-all-movies-and-shows-in-plex-to-use-english-non-forced-subtitles/825871)

## Screenshots:
##### Plex subtitle dropdown after script is done running:
![Plex Subtitle Dropdown](https://i.imgur.com/BNOlwtL.png)
##### PlexPreferNonForcedSubs.py script in action:
![PlexPreferNonForcedSubs.py Script in Action](https://i.imgur.com/2l6DuU6.png)

## Donations:
Like this script? Buy me a coffee! ☕ <br>
Want to more scripts like this? Contact me on [Twitter](https://twitter.com/RileyxBell) <br>
__Cashapp__: $rileyxx <br>
__Venmo__: @rileyxx <br>
__Amazon wishlist__: https://www.amazon.com/hz/wishlist/ls/WURF5NWZ843U <br>
__Bitcoin__: 32r85q3GV1ghAgAFNJ2e4tAxK176BN1Zwq <br>
__Monero__: 43841oakvAXNUVgpMG8iqnPWUiMSQBMoEaeKRvNqzjBcenpcWXuD9hFXCtbB5fpVoNURU11NfVgH9bnxDWGhawHq1pu4JeZ <br>
__Ethereum__: 0xFA264dFF8db79C30fF006479c2f6023f9860B0B8 <br>

