from bs4 import BeautifulSoup
import urllib2

url = "https://www.nasdaq.com/symbol/aapl/historical"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")

#print soup.prettify()
#final_link. soup.p.a
#final_link.decompose()

trs = soup.find_all('tr')


for tr in trs:

    tds = tr.find_all('td')

    try:
        close_price = float(tds[4].get_text())
        date = str(tds[0].get_text())
        date = date.replace("\r", "")
        date = date.replace("\n", "")
        date = date.replace(" ", "")
    except:
        continue

    print(close_price, date)
