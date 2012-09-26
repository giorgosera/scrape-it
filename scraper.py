from BeautifulSoup import BeautifulSoup
import urllib2
import datetime
from mongoengine import *
from mongoengine.queryset import DoesNotExist
from model import Deal, DealHistory

connect('MissMason')

html = urllib2.urlopen("http://www.groupon.co.uk/deals/national-deal/Saverstore/10832959").read()
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

try: 
	deal = Deal.objects(title=title).get()
except DoesNotExist, e:
	deal = Deal()
	deal.title = title
	deal.price = price

deal_history = DealHistory()
deal_history.time = date
deal_history.quantity = amount_sold
deal.deal_history.append(deal_history)

deal.save()

print deal.title
for item in deal.deal_history:
	print item.time
	print item.quantity
	print '------------------'

