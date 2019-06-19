# coding: UTF-8
import urllib.request
import sys
import os
import requests
import json
import re
import LoadConfig as lc
import send_slack as ss

from bs4 import BeautifulSoup
from io import BytesIO

def get_tv_ranking(conf):
    """
    スクレイピングのメイン処理
    @param 設定ファイルのインスタンス
    @return 送信したいメッセージの配列
    """
    ret = []
    url = conf.tvranking_url
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find_all("div", {"class" : "top10_table hidden-xs"})

    for genre in table:
        category = "=== "
        category += re.sub('^[0-9]\.','', genre.find("h4", {"class" : "rt_category_title"}).string)
        # ドラマランキング以外はスキップ
        if (category != "=== ドラマ【関東地区】"): continue
        ret.append(category)
        name = genre.find_all("td", {"height": "25"})
        per = genre.find_all("td", {"class": "xl65"})
        for i in range(len(name)):
            ret.append('{} : {}'.format(per[i].string, name[i].string))

    return ret

def main(argv):
    # 設定ファイル読み込み
    c = lc.LoadConfig()

    # 実際のスクレイピング処理
    L = get_tv_ranking(c)

    # Slackへ通知
    ss.send_slack(L, c)

if __name__ == '__main__':
    main(sys.argv)
