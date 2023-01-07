# PlexDefaultSubtitleChanger


## Short description:
This python script will set all movies and shows in your local Plex library to English non forced subtitles by default. 

## Long description:
This script was created with the help of [ChatGPT Open AI](https://chat.openai.com/chat) and further edited and completed by me. It uses [Plex Python Api](https://python-plexapi.readthedocs.io/en/latest/). It will set all movies and shows in your local Plex library to English non forced subtitles by default. Assuming your Plex subtitles settings are setup in your server settings Plex will default to Forced Subtitles by default when they are available for a given item. Plex will not allow you to prefer non forced subtitles natively hence why this script was created.

This script is confirmed tested and working. Feel free to use this code for your own purposes. I will be running this code periodically on my home server along with some of my other neat little plex scripts like [Plex Auto Delete](https://github.com/Casvt/Plex-scripts/blob/main/changing_settings/plex_auto_delete.py). Thanks to [all](https://stackoverflow.com/questions/75027919/python-script-to-set-all-subtitles-for-movies-shows-in-plex-to-english-non-for) who helped! If you use this script and run into any bugs feel free to open an issue. Cheers!

## Instructions:
##### Windows:
To use this script on Windows. Simply install latest version of [Python](https://www.python.org/downloads/). 
1. Download the latest .py script from the [releases](https://github.com/RileyXX/PlexDefaultSubtitleChanger/releases) page. 
2. Replace xxxxxxx in the script with your [plex api token](https://www.plexopedia.com/plex-media-server/general/plex-token/).
3. Make sure Plex media server is running locally then run the script and watch it work its magic.

##### Note:
This script should work fine on any other operating system. No need to make any changes.

## Also posted on:
* [Stackoverflow](https://stackoverflow.com/q/75027919/9196825)
* [Reddit](https://www.reddit.com/r/PleX/comments/105gdh7/python_code_to_set_all_movies_and_shows_in_plex/)

## Screenshots:
##### Plex subtitle dropdown after script is done running:
![Plex Subtitle Dropdown](https://i.imgur.com/BNOlwtL.png)
##### PlexPreferNonForcedSubs.py script in action:
![PlexPreferNonForcedSubs.py Script in Action](https://i.imgur.com/2l6DuU6.png)
