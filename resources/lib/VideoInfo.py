

import xbmcgui


class VideoInfo:
    def __init__(self, url: str, list_item: xbmcgui.ListItem):
        self._url = str(url),
        self._list_item = list_item

    def get_url(self) -> str:
        return str(self._url)

    def get_list_item(self):
        return self._list_item
