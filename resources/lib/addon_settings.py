from typing import Optional

import xbmcaddon

from resources.lib.model import Args


class AddonSettings:
    def __init__(self,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 session_id: Optional[str] = None,
                 auth_token: Optional[str] = None,
                 device_id: Optional[str] = None,
                 addon_id: Optional[str] = None,
                 addon: Optional[xbmcaddon.Addon] = None,
                 addon_name: Optional[str] = None
                 ):
        self._username: str = username
        self._password: str = password
        self._session_id: str = session_id
        self._auth_token: str = auth_token
        self._device_id: str = device_id
        self._addon_id: str = addon_id
        self._addon: xbmcaddon.Addon = addon
        self._addon_name: str = addon_name

    @property
    def username(self) -> Optional[str]:
        return self._username

    @username.setter
    def username(self, username: Optional[str]) -> None:
        self._username = username

    @property
    def password(self) -> Optional[str]:
        return self._password

    @password.setter
    def password(self, password: Optional[str]) -> None:
        self._password = password

    @property
    def session_id(self) -> Optional[str]:
        return self._session_id

    @session_id.setter
    def session_id(self, session_id: Optional[str]) -> None:
        self._session_id = session_id

    @property
    def auth_token(self) -> Optional[str]:
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token: Optional[str]) -> None:
        self._auth_token = auth_token

    @property
    def device_id(self) -> Optional[str]:
        return self._device_id

    @device_id.setter
    def device_id(self, device_id: Optional[str]) -> None:
        self._device_id = device_id
        self._addon.setSetting("device_id", self._device_id)

    @property
    def addon_id(self) -> Optional[str]:
        return self._addon_id

    @addon_id.setter
    def addon_id(self, addon_id: Optional[str]) -> None:
        self._addon_id = addon_id

    @property
    def addon(self) -> Optional[xbmcaddon.Addon]:
        return self._addon

    @addon.setter
    def addon(self, addon: Optional[xbmcaddon.Addon]) -> None:
        self._addon = addon

    @property
    def addon_name(self) -> Optional[str]:
        return self._addon_name

    @addon_name.setter
    def addon_name(self, addon_name: Optional[str]) -> None:
        self._addon_name = addon_name

    @property
    def subtitle(self) -> str:
        subtitle_key = self._addon.getSetting("subtitle_language")
        return self.SUBTITLE_LANGUAGE_MAP.get(subtitle_key)

    SUBTITLE_LANGUAGE_MAP = {
        "0": "enUS",
        "1": "enGB",
        "2": "esLA",
        "3": "esES",
        "4": "ptBR",
        "5": "ptPT",
        "6": "frFR",
        "7": "deDE",
        "8": "arME",
        "9": "itIT",
        "10": "ruRU",
    }

    def set_addon_setting_device_id(self, device_id: str) -> None:
        self._addon.setSetting("device_id", device_id)

    def __str__(self) -> str:
        return (
            f"AddonSettings(\n"
            f"\tusername={self.username},\n"
            f"\tpassword={'***' if self.password else None},\n"
            f"\tsession_id={'***' if self.session_id else None},\n"
            f"\tauth_token={'***' if self.auth_token else None},\n"
            f"\tdevice_id={'***' if self.device_id else None},\n"
            f"\taddon_id={self.addon_id},\n"
            f"\taddon_name={self.addon_name}\n"
            f")"
        )

    @classmethod
    def create_from_args(cls, args) -> 'AddonSettings':
        return cls(
            username=args._addon.getSetting("crunchyroll_username"),
            password=args._addon.getSetting("crunchyroll_password"),
            session_id=args._addon.getSetting("session_id"),
            auth_token=args._addon.getSetting("auth_token"),
            device_id=args._addon.getSetting("device_id"),
            addon_id=args._addonid,
            addon=args._addon,
            addon_name=args._addonname,
        )
