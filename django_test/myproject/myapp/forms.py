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
