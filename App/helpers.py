import datetime
from typing import Union, Any, Optional

from App import Application
from App.Core.Cache import CacheManager
from App.Services.MimeConvertor import MimeConvertor
from App.Core.Utils.ExecLater import ExecLater
from App.Core.Network import NetworkManager
from App.Core.Console import Output
from App.Core.DB import Connection
from App.Core.Logger import Log
from App.Core import Platform, Machine, Config
from App.Core import Event
from App.Core import MimeTypeConfig


def app(_type: Application.ApplicationType = None) -> Application:
    return Application(_type)


def config(dot_path: Optional[str] = None, value=None) -> Union[Config, Any]:
    _config: Config = app().get('config')

    if dot_path is None:
        return _config

    if value is None:
        return _config.get(dot_path)

    _config.set(dot_path, value)


def cache(
    dot_path: Optional[str] = None,
    value: Union[list, str, int, float, dict, tuple, None] = None
) -> Union[list, str, int, float, dict, tuple, CacheManager, None]:
    _cache: CacheManager = app().get('cache')

    if dot_path is None:
        return _cache

    if value is None:
        return _cache.get(dot_path)

    _cache.set(dot_path, value)


def events() -> Event:
    return app().get('events')


def env(key: str, default: Any = None) -> Any:
    data = app().get('env').get(key)

    return default if data is None else data


def logger() -> Log:
    return app().get('log')


def network_manager() -> NetworkManager:
    return app().get('network.manager')


def later(microseconds: float, func: callable):
    ExecLater(microseconds, func).start()


def in_thread(func: callable):
    later(0, func)


def console() -> Output:
    return app().get('console.output')


def now() -> datetime.datetime:
    return datetime.datetime.now()


def db() -> Connection:
    return app().get('db')


def platform() -> Platform:
    return app().get('platform')


def machine() -> Machine:
    return app().get('machine')


def mime() -> MimeTypeConfig:
    return app().get('mime')


def mime_convertor() -> MimeConvertor:
    return app().get('mime.convertor')


def start_server():
    app().call(['network.manager', 'start_server'])




