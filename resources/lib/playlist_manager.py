import xbmc

# Create a global playlist object
playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)


def add_to_playlist(url, list_item, index):
    """
    Add item to the global playlist.
    """
    playlist.add(url, list_item, index)


def clear_playlist():
    """
    Clear the global playlist.
    """
    playlist.clear()


def get_playlist():
    """
    Retrieve the global playlist.
    """
    return playlist

def get_playlist_size():
    return playlist.size()
