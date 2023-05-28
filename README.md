# PlexPreferNonForcedSubs

## Short Description
This Python script sets all movies and shows in your local Plex library to English non-forced subtitles by default. Please note, this script does not download subtitles, it simply changes the default track for existing subs in your library. It designed to work on Python 3.5 or later and compatible on any operating system where [Python](https://www.python.org/downloads/) is installed (Windows, macOS, Linux, etc).

## Long Description
This script utilizes [Plex Python API](https://github.com/pkkid/python-plexapi) and sets all movies and shows in your local Plex library to English non-forced subtitles by default. The subtitle preferences will be applied to your Plex profile and remembered on other devices. By default, Plex prefers forced subtitles when available for a given item. However, Plex does not natively allow you to prefer non-forced subtitles, which is why this script was created. 

The script has been thoroughly tested and confirmed to be working. Feel free to use the code for your own purposes. I will be running this script periodically on my home server along with some other cool scripts. If you're interested, see below for my other [recommended projects](https://github.com/RileyXX/PlexPreferNonForcedSubs#other-recommended-projects). 

If you encounter any bugs while using this script, please open an [issue](https://github.com/RileyXX/PlexPreferNonForcedSubs/issues) so it can be properly investigated.

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
6. (Optional) If you have not yet setup your preferred subtitle settings in Plex, it is recommended to do so if you want English subs always enabled when available. To avoid overriding manual subtitle selection, the script will not set subtitle tracks to English when the subtitle tracks are set to Off or None. To change your default subtitle settings in Plex, navigate to [Plex Settings](https://app.plex.tv/desktop/#!/settings/account) > Account > Audio & Subtitle Settings > Set your preferred subtitle language to "English" and "Always Enabled". See [screenshot](https://user-images.githubusercontent.com/49823202/241563899-7e6b69d3-52c9-40f2-8386-20d3bd5c04b0.png).

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
- [Reddit](https://www.reddit.com/r/PleX/comments/13ttswd/tool_for_setting_default_subtitles_to_english/)
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

## Other Recommended Projects:

| Project Name | Description |
|--------------|-------------|
| [PlexTraktSync](https://github.com/Taxel/PlexTraktSync) | A script that syncs user watch history and ratings between Trakt and Plex (without needing a PlexPass or Trakt VIP subscription). |
| [IMDB-Trakt-Syncer](https://github.com/RileyXX/IMDB-Trakt-Syncer) | A script that syncs user watchlist, ratings, and comments both ways between Trakt and IMDB. |
| [TMDB-Trakt-Syncer](https://github.com/RileyXX/TMDB-Trakt-Syncer) | A script that syncs user watchlist and ratings both ways between Trakt and TMDB. |
| [PlexPreferNonForcedSubs](https://github.com/RileyXX/PlexPreferNonForcedSubs) | A script that sets all movies and shows in your local Plex library to English non-forced subtitles by default. |
| [Casvt / PlexAutoDelete](https://github.com/Casvt/Plex-scripts/blob/main/changing_settings/plex_auto_delete.py) | A script for automatically deleting watched content from Plex. |
| [Netflix-to-Trakt-Import](https://github.com/jensb89/Netflix-to-Trakt-Import) | A tool to import your Netflix viewing history into Trakt. |
| [trakt-tv-backup](https://darekkay.com/blog/trakt-tv-backup/) | A command-line tool for backing up your Trakt.tv data. |
| [blacktwin / JBOPS](https://github.com/blacktwin/JBOPS) | A collection of scripts and tools for enhancing and automating tasks in Plex. |
| [Casvt / Plex-scripts](https://github.com/Casvt/Plex-scripts) | A collection of useful scripts for Plex automation and management. |
| [trakt---letterboxd-import](https://github.com/jensb89/trakt---letterboxd-import) | A tool to import your Letterboxd ratings and watchlist into Trakt. |
| [TraktRater](https://github.com/damienhaynes/TraktRater/) | A tool to help users transfer user episode, show, and movie user ratings and watchlists from multiple media database sites around the web. |
| [TvTimeToTrakt](https://github.com/lukearran/TvTimeToTrakt) | A tool to sync your TV Time watch history with Trakt.tv. |
| [Plex Media Server](https://www.plex.tv/media-server-downloads/#plex-app) | A media server software to organize and stream your personal media collection. |
| [Radarr](https://github.com/Radarr/Radarr) | A movie collection manager and downloader for various platforms. |
| [Sonarr](https://github.com/Sonarr/Sonarr) | A TV show collection manager and downloader for various platforms. |
| [Jackett](https://github.com/Jackett/Jackett) | A proxy server that provides API support for various torrent trackers commonly used with Radarr and Sonarr. |
| [qBittorrent](https://github.com/qbittorrent/qBittorrent) | A free and open-source BitTorrent client. |
| [Mullvad VPN](https://github.com/mullvad/mullvadvpn-app) | An open-source VPN client for Mullvad VPN service with port forwarding support. Great VPN for torrents. |
| [Overseerr](https://github.com/sct/overseerr) | A request management and media discovery tool for your home media server. |
| [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) | A reverse proxy solution to bypass Cloudflare protection and access websites commonly used with Jackett. |
| [youtube-dl](https://github.com/ytdl-org/youtube-dl) | A command-line program to download videos from YouTube and other sites. |

