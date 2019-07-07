# coding: UTF-8
import urllib.request
import sys
import LoadConfig as lc
import send_slack as ss

from bs4 import BeautifulSoup

def get_hatebu_ranking(conf):
    """
    スクレイピングのメイン処理
    @param 設定ファイルのインスタンス
    @return 送信したいメッセージの配列
    """
    url = conf.hatebu_url
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    article_list = soup.find_all("div", {"class" : "entrylist-contents-main"})

    ret = []
    for article in article_list[:10]:
        title_info = article.find("a", {"class" : "js-keyboard-openable"})
        title = title_info.get("title")
        ref = title_info.get("href")
        users = article.find("a", {"class" : "js-keyboard-entry-page-openable"}).find("span").contents[0]
        tmp = "[{} users] {} ({})".format(users, title, ref)
        ret.append(tmp)
    return ret

def main(argv):
    # 設定ファイル読み込み
    c = lc.LoadConfig()

    # 実際のスクレイピング処理
    L = get_hatebu_ranking(c)

    # Slackへ通知
    ss.send_slack(L, c)

if __name__ == '__main__':
    main(sys.argv)
