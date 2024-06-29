import os

from . import __version__ as version

DEFAULT_BASE_URL = 'https://esp.evident.io'
DEFAULT_HTTP_PROXY = None
DEFAULT_PER_PAGE = 20
# add version to the user agent
DEFAULT_USER_AGENT = 'Python SDK {version}'.format(version=version)


# borrowed from kennethreitz's legit
class Settings(object):
    _singleton = {}
    __attrs__ = tuple()

    def __init__(self, **kwargs):
        super(Settings, self).__init__()
        self.__dict__ = self._singleton

    def __call__(self, *args, **kwargs):
        r = self.__class__()
        r.__cache = self.__dict__.copy()
        map(self.__cache.setdefault, self.__attrs__)
        self.__dict__.update(*args, **kwargs)
        return r

    def __enter__(self):
        pass

    def __exit__(self, *args):
        self.__dict__.update(self.__cache.copy())
        del self.__cache

    def __getattribute__(self, key):
        if key in object.__getattribute__(self, '__attrs__'):
            try:
                return object.__getattribute__(self, key)
            except AttributeError:
                return None
        return object.__getattribute__(self, key)


settings = Settings()  # create the singleton

settings.access_key_id = os.environ.get('ESP_ACCESS_KEY_ID', None)
settings.secret_access_key = os.environ.get('ESP_SECRET_ACCESS_KEY', None)
settings.host = os.environ.get('ESP_HOST', DEFAULT_BASE_URL)
settings.api_prefix = '/api/v2'
settings.user_agent = DEFAULT_USER_AGENT
settings.per_page = DEFAULT_PER_PAGE
settings.http_proxy = DEFAULT_HTTP_PROXY
