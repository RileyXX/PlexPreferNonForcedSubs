from plexapi.server import PlexServer
import requests
import xml.etree.ElementTree as ET

# Connect to the Plex server
baseurl = 'http://localhost:32400'
token = 'xxxxxxxx'
plex = PlexServer(baseurl, token)

# Set all movies to use English non-forced subtitles if available, otherwise print no subtitles found
for movie in plex.library.section('Movies').all():
    movie.reload()
    # Get all English subtitle streams for the current movie
    english_subs = [stream for stream in movie.subtitleStreams() if stream.languageCode == 'eng']
    # Filter out any English subtitle streams that are marked as forced
    # or have the word "forced" in their title (case insensitive)
    non_forced_english_subs = [stream for stream in english_subs if not stream.forced or (hasattr(stream, 'title') and stream.title is not None and 'forced' not in stream.title.lower())]
    # Get all English subtitle streams that are marked as forced
    forced_english_subs = [stream for stream in english_subs if stream.forced or (hasattr(stream, 'title') and stream.title is not None and 'forced' in stream.title.lower())]
    part = movie.media[0].parts[0]
    partsid = part.id
    if forced_english_subs and non_forced_english_subs:
        # If movies has forced english subs AND non forced english subs THEN set show to prefer english non forced subs
        # Send a request to the Plex client to set the subtitle stream
        url = f'{baseurl}/library/parts/{partsid}?subtitleStreamID={non_forced_english_subs[0].id}&allParts=1'
        headers = {'X-Plex-Token': token}
        requests.put(url, headers=headers)
        print(f'\033[92m{movie.title}: Setting non forced English subtitles.\033[0m')
    elif non_forced_english_subs and not forced_english_subs:
        print(f'{movie.title}: Has English subtitles but no English forced subtitles. No subtitle changes.')
    elif not non_forced_english_subs and not forced_english_subs and not forced_english_subs:
        print(f'{movie.title}: No English subtitles found. No subtitle changes.')
    else:
        print(f'{movie.title}: No subtitle changes.')

# Set all TV shows to use English non-forced subtitles if available, otherwise print no subtitles found
for show in plex.library.section('TV Shows').all():
    show.reload()
    for episode in show.episodes():
        show.reload()
        episode.reload()
        # Get all English subtitle streams for the current show
        english_subs = [stream for stream in episode.subtitleStreams() if stream.languageCode == 'eng']
        # Filter out any English subtitle streams that are marked as forced
        # or have the word "forced" in their title (case insensitive)
        non_forced_english_subs = [stream for stream in english_subs if not stream.forced or (hasattr(stream, 'title') and stream.title is not None and 'forced' not in stream.title.lower())]
        # Get all English subtitle streams that are marked as forced
        forced_english_subs = [stream for stream in english_subs if stream.forced or (hasattr(stream, 'title') and stream.title is not None and 'forced' in stream.title.lower())]
        part = episode.media[0].parts[0]
        partsid = part.id
        if forced_english_subs and non_forced_english_subs:
            # If show has forced english subs AND non forced english subs THEN set show to prefer english non forced subs
            # Send a request to the Plex client to set the subtitle stream
            url = f'{baseurl}/library/parts/{partsid}?subtitleStreamID={non_forced_english_subs[0].id}&allParts=1'
            headers = {'X-Plex-Token': token}
            requests.put(url, headers=headers)
            print(f'\033[92m{show.title} - {episode.title}: Setting non forced English subtitles.\033[0m')
        elif non_forced_english_subs and not forced_english_subs:
            print(f'{show.title} - {episode.title}: Has English subtitles but no english forced subtitles. No subtitle changes.')
        elif not non_forced_english_subs and not forced_english_subs and not forced_english_subs:
            print(f'{show.title} - {episode.title}: No English subtitles found. No subtitle changes.')
        else:
            print(f'{show.title} - {episode.title}: No subtitle changes.')
