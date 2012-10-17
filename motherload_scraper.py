from BeautifulSoup import BeautifulSoup
import urllib2
import datetime
from mongoengine import *
from mongoengine.queryset import DoesNotExist
from model import Deal, DealHistory

connect('Giorgos')

html = urllib2.urlopen("http://www.dft.gov.uk/fyn/ordit.php").read()
soup = BeautifulSoup(html)

#Get table
table = soup.table

#Get body
body = table.tbody

for i, row in enumerate(body.findAll('tr')): 

	if i % 2 == 1:#if the index is odd skip (skip the table shit entries)
		continue
	columns = row.findAll("td")
	school_name_column = columns[0]
	contact_column = columns [1]

	school_name = school_name_column.h4.string

	school_name_column.br.extract()
	address1 = school_name_column.h4.nextSibling
	address2 = address1.nextSibling
	address3 = address2.nextSibling
	address4 = address3.nextSibling
 	address5 = address4.nextSibling

 	contact_name = contact_column.strong
 	
 	br = contact_name.nextSibling
 	contact_tel = br.nextSibling
 	br = contact_tel.nextSibling
 	href = br.nextSibling
 	contact_email = href.nextSibling
 	br = contact_email.nextSibling
 	href = br.nextSibling
 	website = href.nextSibling

 	print "--------------------------------------------"
	print contact_name.string.strip()
	print contact_tel.string.strip()
 	if contact_email.string != None:
		print contact_email.string.strip()
	
	if website.string != None:
		print website.string.strip() 
	print "--------------------------------------------"

#Get deal's title
# title_tag = soup.find("div", {"id": "contentDealTitle"})
# title = title_tag.h1.a.string.strip()

# #Get price
# price_tag = soup.find("span", {"class": "price"})
# price_tag = price_tag.find("span", {"class": "noWrap"})
# price = price_tag.string.rpartition(';')[2]

# #Get quantity sold
# amount_sold_tag = soup.find("div", {"class": "soldAmount"})
# amount_sold_tag = amount_sold_tag.find("span", {"id": "jDealSoldAmount"})
# amount_sold = amount_sold_tag.string.rpartition(';')[2]

# #Record date
# date = datetime.datetime.now()

# try: 
# 	deal = Deal.objects(title=title).get()
# except DoesNotExist, e:
# 	deal = Deal()
# 	deal.title = title
# 	deal.price = price

# deal_history = DealHistory()
# deal_history.time = date
# deal_history.quantity = amount_sold
# deal.deal_history.append(deal_history)

# deal.save()

# print deal.title
# for item in deal.deal_history:
# 	print item.time
# 	print item.quantity
# 	print '------------------'

