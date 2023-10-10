import xbmc
import xbmcgui

from resources.lib.VideoInfo import VideoInfo


def get_next_info(current_episode: xbmcgui.ListItem, next_episode: xbmcgui.ListItem, next_episode_url: str):

    current_episode_info: xbmc.InfoTagVideo = current_episode.getVideoInfoTag()
    next_episode_info: xbmc.InfoTagVideo = next_episode.getVideoInfoTag()

    next_info = dict(
        current_episode=dict(
            episodeid=current_episode_info.getDbId(),
            tvshowid=current_episode_info.getDbId(),
            title=current_episode_info.getTitle(),
            art={
                'thumb': current_episode.getArt("thumb"),
                'banner': current_episode.getArt("thumb"),
                'fanart': current_episode.getArt("fanart"),
                'icon': current_episode.getArt("thumb"),
                'poster': current_episode.getArt("thumb"),
            },
            season=current_episode_info.getSeason(),
            episode=current_episode_info.getEpisode(),
            showtitle=current_episode_info.getTVShowTitle(),
            plot=current_episode_info.getPlot(),
            playcount=current_episode_info.getPlayCount(),
            rating=current_episode_info.getRating(),
            firstaired=current_episode_info.getFirstAired(),
            runtime="",  # NOTE: This is optional
        ),
        next_episode=dict(
            episodeid=next_episode_info.getDbId(),
            tvshowid=next_episode_info.getDbId(),
            title=next_episode_info.getTitle(),
            art={
                'thumb': current_episode.getArt("thumb"),
                'banner': current_episode.getArt("thumb"),
                'fanart': current_episode.getArt("fanart"),
                'icon': current_episode.getArt("thumb"),
                'poster': current_episode.getArt("thumb"),
            },
            season=next_episode_info.getSeason(),
            episode=next_episode_info.getEpisode(),
            showtitle=next_episode_info.getTVShowTitle(),
            plot=next_episode_info.getPlot(),
            playcount=next_episode_info.getPlayCount(),
            rating=next_episode_info.getRating(),
            firstaired=next_episode_info.getFirstAired(),
            runtime="",  # NOTE: This is o # NOTE: This is optional
        ),
        # NOTE: You need to provide either `play_info` or `play_url`
        play_url=next_episode_url,
        #    play_info=dict(
        #        item_id=next_item_details.id,
        #    ),
        notification_time=30,  # NOTE: This is optional
        #    notification_offset=notification_offset,
    )

    return next_info

def upnext_signal(sender, next_info):
    """Send a signal to Kodi using JSON RPC"""
    from base64 import b64encode
    from json import dumps
    data = [to_unicode(b64encode(dumps(next_info).encode()))]
    notify(sender=sender + '.SIGNAL', message='upnext_data', data=data)

def notify(sender, message, data):
    """Send a notification to Kodi using JSON RPC"""
    result = jsonrpc(method='JSONRPC.NotifyAll', params=dict(
        sender=sender,
        message=message,
        data=data,
    ))
    if result.get('result') != 'OK':
        xbmc.log('Failed to send notification: ' + result.get('error').get('message'), 4)
        return False
    return True

def jsonrpc(**kwargs):
    """Perform JSONRPC calls"""
    from json import dumps, loads
    if kwargs.get('id') is None:
        kwargs.update(id=0)
    if kwargs.get('jsonrpc') is None:
        kwargs.update(jsonrpc='2.0')
    return loads(xbmc.executeJSONRPC(dumps(kwargs)))

def to_unicode(text, encoding='utf-8', errors='strict'):
    """Force text to unicode"""
    if isinstance(text, bytes):
        return text.decode(encoding, errors=errors)
    return text
