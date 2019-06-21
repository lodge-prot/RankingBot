#
# モック
#

import urllib.request, urllib.error
from bs4 import BeautifulSoup

url = "https://github.com/trending/python"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

BASE = "https://github.com"
rank_list = soup.find_all("h1", {"class" : "h3 lh-condensed"})

for i in range(1, len(rank_list)+1):
    repo_url = '{}{}'.format(BASE, rank_list[i-1].find("a").get("href"))
    print('[{}] : {}'.format(i, rank_list[i-1].find("a").get_text().strip().replace(' ', '')))
    print('({})'.format(repo_url))
