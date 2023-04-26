from plexapi.server import PlexServer
from plexapi.media import SubtitleStream

# Connect to Plex Media Server. Replace xxxxxxxx below with your Plex token. How to get token: https://www.plexopedia.com/plex-media-server/general/plex-token/
baseurl = 'http://localhost:32400'
token = 'PLEX_TOKEN'
try:
    with open('token.txt', 'r') as f:
        token = f.read().strip()
except FileNotFoundError:
    pass

if token == 'PLEX_TOKEN':
    # Prompt user to enter Plex token
    token = input("Enter your Plex token: ")
    # Save token to token.txt in the same folder as the script
    with open('token.txt', 'w') as f:
        f.write(token)

plex = PlexServer(baseurl, token)

table_headers = ['Title', 'Year', 'Status', 'Changes']
title_width = 70
year_width = 5
status_width = 20
changes_width = 8

print("\n" + "-" * 114 + "\nMovies\n" + "-" * 114)
print(f'\033[1m\033[96m{" | ".join([h.ljust(title_width if i == 0 else year_width if i == 1 else status_width if i == 2 else changes_width) for i, h in enumerate(table_headers)])}\033[0m')

for section in plex.library.sections():
    if section.type == 'movie':
        for movie in section.all():
            movie.reload()
            english_subs = [stream for stream in movie.subtitleStreams() if stream.languageCode == 'eng']
            non_forced_english_subs = [stream for stream in english_subs if not stream.forced or (hasattr(stream, 'title') and stream.title is not None and 'forced' not in stream.title.lower())]
            forced_english_subs = [stream for stream in english_subs if stream.forced or (hasattr(stream, 'title') and stream.title is not None and 'forced' in stream.title.lower())]
            part = movie.media[0].parts[0]
            partsid = part.id
            if forced_english_subs and non_forced_english_subs:
                non_forced_english_subs[0].setDefault()
                print(f'\033[92m{movie.title[:title_width].ljust(title_width)} | {str(movie.year).ljust(year_width)} | {"English (Non-Forced)".ljust(status_width)} | {"Y".ljust(changes_width)}\033[0m')
            elif non_forced_english_subs and not forced_english_subs:
                print(f'{movie.title[:title_width].ljust(title_width)} | {str(movie.year).ljust(year_width)} | {"English".ljust(status_width)} | {"N".ljust(changes_width)}')
            elif not non_forced_english_subs and not forced_english_subs:
                print(f'\033[91m{movie.title[:title_width].ljust(title_width)} | {str(movie.year).ljust(year_width)} | {"No Subtitles Found".ljust(status_width)} | {"N".ljust(changes_width)}\033[0m')
            else:
                print(f'\033[91m{movie.title[:title_width].ljust(title_width)} | {str(movie.year).ljust(year_width)} | {"English (Forced)".ljust(status_width)} | {"N (Error)".ljust(changes_width)}\033[0m')


table_headers = ['Title', 'Year', 'Season #', 'Episode #', 'Status', 'Changes']
title_width = 42
year_width = 5
season_width = 11
episode_width = 11
status_width = 20
changes_width = 8
season_row_width = 4
episode_row_width = 3

print("\n" + "-" * 114 + "\nShows\n" + "-" * 114)
print(f'\033[1m\033[96m{" | ".join([h.ljust(title_width if i == 0 else year_width if i == 1 else season_width if i == 2 else episode_width if i == 3 else status_width if i == 4 else changes_width) for i, h in enumerate(table_headers)])}\033[0m')

for section in plex.library.sections():
    if section.type == 'show':
        for show in section.all():
            show.reload()
            for episode in show.episodes():
                show.reload()
                episode.reload()
                english_subs = [stream for stream in episode.subtitleStreams() if stream.languageCode == 'eng']
                non_forced_english_subs = [stream for stream in english_subs if not stream.forced or (hasattr(stream, 'title') and stream.title is not None and 'forced' not in stream.title.lower())]
                forced_english_subs = [stream for stream in english_subs if stream.forced or (hasattr(stream, 'title') and stream.title is not None and 'forced' in stream.title.lower())]
                part = episode.media[0].parts[0]
                partsid = part.id
                if forced_english_subs and non_forced_english_subs:
                    non_forced_english_subs[0].setDefault()
                    print(f'\033[92m{show.title[:title_width].ljust(title_width)} | {str(show.year).ljust(year_width)} | {"Season " + str(episode.seasonNumber).ljust(season_row_width)} | {"Episode " + str(episode.index).ljust(episode_row_width)} | {"English (Non-Forced)".ljust(status_width)} | {"Y".ljust(changes_width)}\033[0m')
                elif non_forced_english_subs and not forced_english_subs:
                    print(f'{show.title[:title_width].ljust(title_width)} | {str(show.year).ljust(year_width)} | {"Season " + str(episode.seasonNumber).ljust(season_row_width)} | {"Episode " + str(episode.index).ljust(episode_row_width)} | {"English".ljust(status_width)} | {"N".ljust(changes_width)}')
                elif not non_forced_english_subs and not forced_english_subs and not forced_english_subs:
                    print(f'\033[91m{show.title[:title_width].ljust(title_width)} | {str(show.year).ljust(year_width)} | {"Season " + str(episode.seasonNumber).ljust(season_row_width)} | {"Episode " + str(episode.index).ljust(episode_row_width)} | {"No Subtitles Found".ljust(status_width)} | {"N".ljust(changes_width)}\033[0m')
                else:
                    print(f'\033[91m{show.title[:title_width].ljust(title_width)} | {str(show.year).ljust(year_width)} | {"Season " + str(episode.seasonNumber).ljust(season_row_width)} | {"Episode " + str(episode.index).ljust(episode_row_width)} | {"English (Forced)".ljust(status_width)} | {"N (Error)".ljust(changes_width)}\033[0m')