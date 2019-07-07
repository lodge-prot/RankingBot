# coding: UTF-8
import urllib.request
import sys
import os
import requests
import json

from bs4 import BeautifulSoup
from io import BytesIO

def loggin(f):
    """
    Log data flush
    """
    pass

def get_qiita_daily(url):
    """
    Get Daily Ranking of Qiita
    """
    try:
        html = urllib.request.urlopen(url)
    except Exception as ex:
        error_message = str(ex)
        print(error_message)
        sys.exit()

    soup = BeautifulSoup(html, "html.parser")
    j = soup.find("div" , class_="p-home_main mb-3 mr-0@s").find("div")['data-hyperapp-props']
    print(j)


def main(argv):
    get_qiita_daily("https://qiita.com/")

if __name__ == '__main__':
    main(sys.argv)
