from BeautifulSoup import BeautifulSoup
import urllib2

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)


html = urllib2.urlopen("http://www.groupon.co.uk/deals/national-deal/bhs/10353038").read()

soup = BeautifulSoup(html)

price_tag = soup.find("span", {"class": "price"})
amount_tag = price_tag.find("span", {"class": "noWrap"})

print amount_tag.string.rpartition(';')[2]

