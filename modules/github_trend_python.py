import urllib.request as ur
from bs4 import BeautifulSoup as bs
ba="https://github.com"
rl=bs(ur.urlopen(ba+"/trending/python"),'lxml').find_all("h1",{"class":"h3 lh-condensed"},limit=10)
for j,u in enumerate([f'{ba}{rl[i-1].find("a").get("href")}'for i in range(1,len(rl)+1)]): print(f'{j+1:02}:{u}')
