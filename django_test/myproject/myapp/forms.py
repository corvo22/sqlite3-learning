from django import forms
from .models import card

class CardForm(forms.ModelForm):
	
	model = card
	name = forms.CharField(required=True)
	setCode = forms.CharField(required=True)
	setNumber = forms.IntegerField(required=True)
	copies = forms.IntegerField(required=True)
	exlude = ("artist","colors","power","toughness","manaCost","text","subtypes","supertypes","types",)

	class Meta:
		model = card
		fields = ['name', 'setCode', 'setNumber', 'copies']

class SearchForm(forms.ModelForm):

	model = card
	name = forms.CharField(required=False)
	setCode = forms.CharField(required=False)
	colors = forms.CharField(required=False)
	manaCost = forms.IntegerField(required=False)
	power = forms.IntegerField(required=False)
	toughness = forms.IntegerField(required=False)
	subtypes = forms.CharField(required=False)
	keywords = forms.CharField(required=False)
	exlude = ('artist', 'supertypes', 'types',)

	class Meta:
		model = card
		fields = ['name', 'setCode', 'colors', 'manaCost', 'power', 'toughness', 'subtypes', 'keywords']