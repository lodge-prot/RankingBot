# coding: UTF-8
import configparser
import sys
import os

class LoadConfig():
    def __init__(self, f='./setup.ini'):
        self.file = f
        inifile = configparser.ConfigParser()
        inifile.read(self.file, 'UTF-8')
        self.load_config(inifile)

    def load_config(self, inf):
        """
        設定ファイルのマッピング
        """
        self.__version          = inf.get('General', 'VERSION')
        self.__request_timeout  = inf.get('General', 'REQUEST_TIMEOUT')
        self.__sleep_time       = inf.get('General', 'SLEEP_TIME')
        self.__retry_num        = inf.get('General', 'RETRY_NUM')
        self.__max_send_line    = inf.get('General', 'MAX_SEND_LINE')
        self.__slack_web_token  = inf.get('slack', 'SLACK_WEB_TOKEN')
        self.__qiita_url        = inf.get('qiita', 'qiita_url')
        self.__tvranking_url    = inf.get('tvranking', 'tvranking_url')
        self.__hatebu_url       = inf.get('hatebu', 'hatebu_url')

        if (self.__slack_web_token == ""):
            print("The format of 'setup.ini' is incorrect : SLACK_WEB_TOKEN")
            sys.exit()

    @property
    def version(self):
        return self.__version

    @property
    def request_timeout(self):
        return self.__request_timeout

    @property
    def retry_num(self):
        return self.__retry_num

    @property
    def slack_web_token(self):
        return self.__slack_web_token

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

    @property
    def max_send_line(self):
        return self.__max_send_line

    @property
    def tvranking_url(self):
        return self.__tvranking_url

    @sleep_time.setter
    def posit(self, sleep_time):
        self.__sleep_time = sleep_time
        return 0

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
