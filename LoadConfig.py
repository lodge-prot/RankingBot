import configparser
import sys
import os

class LoadConfig():
    def __init__(self, f):
        self.file = f
        inifile = configparser.ConfigParser()
        inifile.read(self.file, 'UTF-8')
        self.load_config(inifile)

    def load_config(self, inf):
        self.__slack_web_token  = inf.get('slack', 'SLACK_WEB_TOKEN')
        self.__qiita_url        = inf.get('qiita', 'qiita_url')
        self.__hatebu_url       = inf.get('hatebu', 'hatebu_url')
        self.__sleep_time       = inf.get('General', 'SLEEP_TIME')

    @property
    def slack_web_token(self):
        return self.__slack_web_token

    @property
    def qiita_url(self):
        return self.__qiita_url

    @property
    def hatebu_url(self):
        return self.__hatebu_url

    @property
    def sleep_time(self):
        return self.__sleep_time

    def get_platform():
        # Cross compiling
        if "_PYTHON_HOST_PLATFORM" in os.environ:
            return os.environ["_PYTHON_HOST_PLATFORM"]

        # Get value of sys.platform
        if sys.platform.startswith('osf1'):
            return 'osf1'
        return sys.platform

    CROSS_COMPILING = ("_PYTHON_HOST_PLATFORM" in os.environ)
    HOST_PLATFORM   = get_platform()
    MS_WINDOWS      = (HOST_PLATFORM == 'win32')
    MACOS           = (HOST_PLATFORM == 'darwin')
    CYGWIN          = (HOST_PLATFORM == 'cygwin')
