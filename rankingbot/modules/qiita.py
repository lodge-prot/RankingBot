# coding: UTF-8
import urllib.request
import sys
import os
import requests
import json
import LoadConfig as lc
import send_slack as ss

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

    di = json.loads(j)

    article_url = ""
    msg_list = []
    for val in di['trend']['edges']:
        tn = val['node']
        article_url = '{}{}/items/{}'.format(url, tn['author']['urlName'], tn['uuid'])
        tmp = '[{}]({})'.format(tn['title'][:17], article_url)
        msg_list.append(tmp)
    return msg_list

def main(argv):
    c = lc.LoadConfig()
    L = get_qiita_daily(c.qiita_url)
    ss.send_slack(L, c)

if __name__ == '__main__':
    main(sys.argv)
