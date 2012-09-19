from mongoengine import Document, StringField, ListField, EmbeddedDocument, DateTimeField, IntField, EmbeddedDocumentField

import datetime

class DealHistory(EmbeddedDocument):
	time = DateTimeField(required = True, default = datetime.datetime.now)
	quantity = IntField(required = True, default = 0)

class Deal(Document):
	meta = {"collection":"DavesDeals"}
	title = StringField(required = True, default = "Sorry Dave")
	price = StringField(required = True, default = "More than you can afford")
	deal_history = ListField(EmbeddedDocumentField(DealHistory), required = True, default = list)

