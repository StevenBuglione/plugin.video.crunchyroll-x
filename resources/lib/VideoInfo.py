from urllib.parse import urlparse, parse_qs, quote_plus, urlencode


class VideoInfo:
    def __init__(self, url: str):
        parsed_url = urlparse(url)
        parsed_qs = parse_qs(parsed_url.query)
        info_dict = {k: parsed_qs[k][0] for k in parsed_qs}

        self.title = info_dict.get('title', '')
        self.tvshowtitle = info_dict.get('tvshowtitle', '')
        self.duration = int(info_dict.get('duration', 0))
        self.episode = int(info_dict.get('episode', 0))
        self.episode_id = info_dict.get('episode_id', '')
        self.collection_id = info_dict.get('collection_id', '')
        self.series_id = info_dict.get('series_id', '')
        self.plot = info_dict.get('plot', '')
        self.plotoutline = info_dict.get('plotoutline', '')
        self.aired = info_dict.get('aired', '')
        self.premiered = info_dict.get('premiered', '')
        self.thumb = info_dict.get('thumb', '')
        self.fanart = info_dict.get('fanart', '')
        self.mode = info_dict.get('mode', '')
        self.genre = info_dict.get('genre', '')
        self.season = int(info_dict.get('season', 0))
        self.status = info_dict.get('status', '')
        self.studio = info_dict.get('studio', '')
        self.year = int(info_dict.get('year', 0))

    def to_url(self, base_url='plugin://plugin.video.crunchyroll/'):
        params = {
            'title': self.title,
            'tvshowtitle': self.tvshowtitle,
            'duration': self.duration,
            'episode': self.episode,
            'episode_id': self.episode_id,
            'collection_id': self.collection_id,
            'series_id': self.series_id,
            'plot': self.plot,
            'plotoutline': self.plotoutline,
            'aired': self.aired,
            'premiered': self.premiered,
            'thumb': self.thumb,
            'fanart': self.fanart,
            'mode': self.mode,
            'genre': self.genre,
            'season': self.season,
            'status': self.status,
            'studio': self.studio,
            'year': self.year
        }
        return base_url + '?' + urlencode(params)

    @property
    def title_url_encoded(self):
        return quote_plus(self.title)

    @property
    def tvshowtitle_url_encoded(self):
        return quote_plus(self.tvshowtitle)

    @property
    def episode_id_url_encoded(self):
        return quote_plus(self.episode_id)

    @property
    def collection_id_url_encoded(self):
        return quote_plus(self.collection_id)

    @property
    def series_id_url_encoded(self):
        return quote_plus(self.series_id)

    @property
    def plot_url_encoded(self):
        return quote_plus(self.plot)

    @property
    def plotoutline_url_encoded(self):
        return quote_plus(self.plotoutline)

    @property
    def aired_url_encoded(self):
        return quote_plus(self.aired)

    @property
    def premiered_url_encoded(self):
        return quote_plus(self.premiered)

    @property
    def thumb_url_encoded(self):
        return quote_plus(self.thumb)

    @property
    def fanart_url_encoded(self):
        return quote_plus(self.fanart)

    @property
    def mode_url_encoded(self):
        return quote_plus(self.mode)

    @property
    def genre_url_encoded(self):
        return quote_plus(self.genre)

    @property
    def status_url_encoded(self):
        return quote_plus(self.status)

    @property
    def studio_url_encoded(self):
        return quote_plus(self.studio)

    def __str__(self):
        return (
            f"title: {self.title}\n"
            f"tvshowtitle: {self.tvshowtitle}\n"
            f"duration: {self.duration}\n"
            f"episode: {self.episode}\n"
            f"episode_id: {self.episode_id}\n"
            f"collection_id: {self.collection_id}\n"
            f"series_id: {self.series_id}\n"
            f"plot: {self.plot}\n"
            f"plotoutline: {self.plotoutline}\n"
            f"aired: {self.aired}\n"
            f"premiered: {self.premiered}\n"
            f"thumb: {self.thumb}\n"
            f"fanart: {self.fanart}\n"
            f"mode: {self.mode}\n"
            f"genre: {self.genre}\n"
            f"season: {self.season}\n"
            f"status: {self.status}\n"
            f"studio: {self.studio}\n"
            f"year: {self.year}\n"
        )

