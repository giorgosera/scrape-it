from BeautifulSoup import BeautifulSoup
import urllib2
import datetime
from mongoengine import *

from model import Deal, DealHistory

connect('MissMason')

html = urllib2.urlopen("http://www.groupon.co.uk/deals/national-deal/Bonusprint/10458922").read()
soup = BeautifulSoup(html)

#Get deal's title
title_tag = soup.find("div", {"id": "contentDealTitle"})
title = title_tag.h1.a.string.strip()

#Get price
price_tag = soup.find("span", {"class": "price"})
price_tag = price_tag.find("span", {"class": "noWrap"})
price = price_tag.string.rpartition(';')[2]

#Get quantity sold
amount_sold_tag = soup.find("div", {"class": "soldAmount"})
amount_sold_tag = amount_sold_tag.find("span", {"id": "jDealSoldAmount"})
amount_sold = amount_sold_tag.string.rpartition(';')[2]

#Record date
date = datetime.datetime.now()

deal = Deal()
deal.title = title
deal.price = price

deal_history = DealHistory()
deal_history.time = date
deal_history.quantity = amount_sold
deal.deal_history.append(deal_history)

deal.save()

print 'Scraping Groupon biatch!'
print '==========================='
print '-->Item: ', title
print '-->Price: ', price
print '-->Quantity sold: ', amount_sold
print '-->Datetime: ', date
print '==========================='

