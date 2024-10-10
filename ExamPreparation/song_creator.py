def add_songs(*args):
    songs = {}
    result = ""
    for song in args:
        title = song[0]
        text = song[1]
        if title not in songs:
            songs[title] = []
        if text:
            songs[title].extend(text)

    for song, lyrics in songs.items():
        result += f"- {song}\n"
        if lyrics:
            result += "\n".join(lyrics) + "\n"

    return result.strip()
