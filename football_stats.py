from bs4 import BeautifulSoup
import urllib2

url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")

#print soup.prettify()
#final_link. soup.p.a
#final_link.decompose()

trs = soup.find_all('tr')

max_number = 0

for tr in trs:

    tds = tr.find_all('td')

    try:
        player = str(tds[0].get_text())
        position = str(tds[1].get_text())
        team = str(tds[2].get_text())
        touchdown = int(tds[6].get_text())
        max_number += 1
    except:
        continue

    print(player, position, team, touchdown)
    if max_number == 20:
        break
