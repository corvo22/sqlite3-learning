from django.db import models

# Create your models here.

class CardManager(models.Manager):
	def create_card(self, card_info):

		new_card = self.create(card_info['name'],card_info['artist'],card_info['colors'],card_info['power'],card_info['toughness'],card_info['manaValue'],card_info['manaCost'],
			card_info['text'],card_info['setcode'],card_info['subtypes'],card_info['supertypes'],card_info['setNumber'])

		return new_card

class card(models.Model):
	name = models.CharField(max_length=128)
	artist = models.CharField(max_length=128)
	colors = models.CharField(max_length=64)
	power = models.IntegerField(null=True)
	toughness = models.IntegerField(null=True)
	manaValue = models.IntegerField()
	manaCost = models.CharField(max_length=65)
	text = models.CharField(max_length=1024)
	setcode = models.CharField(max_length=4)
	subtypes = models.CharField(max_length=64)
	supertypes = models.CharField(max_length=64)
	types = models.CharField(max_length=64)
	setNumber = models.IntegerField()
	copies = models.IntegerField()
	
	objects = CardManager()

	def __str__(self):
		text_representation = self.name
		return text_representation

	def get_attributes(self):
		attribute_list = [
			self.name,
			self.artist,
			self.colors,
			str(self.power),
			str(self.toughness),
			str(self.manaValue),
			self.manaCost,
			self.text,
			self.setcode,
			self.subtypes,
			self.supertypes,
			str(self.setNumber),
			str(self.copies)]

		return attribute_list