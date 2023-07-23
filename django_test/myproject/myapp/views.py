from django.shortcuts import render, redirect
from datetime import date
from .forms import CardForm
from .models import card, CardManager
import sqlite3

# Create your views here.
def myview(request):
	form = CardForm()
	if request.POST:
		form = CardForm(request.POST)
		if form.is_valid():

			qset = (form['name'].value(), form['setCode'].value(), form['setNumber'].value())

			print(form)

			con = sqlite3.connect("AllPrintings.sqlite")
			cur = con.cursor()
			
			entry_keys = ['name','artist','colors','power','toughness','manaValue','manaCost','text','setcode','subtypes','supertypes','types','setNumber','copies']
			entry_values = cur.execute("SELECT name,artist,colors,power,toughness,manaValue,manaCost,text,setcode,subtypes,supertypes,types,number FROM cards WHERE name = ? AND setCode = ? AND number = ?",qset).fetchall()
			
			if entry_values:
				entry_values = list(entry_values[0])
				print(entry_values)
				entry_values.append(int(form['copies'].value()))
				print(entry_values)
				entry_dict = dict(zip(entry_keys,entry_values))
				print(entry_dict)
				entry = card.objects.create(**entry_dict)


				entry.save()

			form = CardForm()

			return redirect('/myapp')

	context	= {'form':form}
	return render(request, "index.html", context)

def card_collection(request):

	'''
	con = sqlite3.connect("db.sqlite3")
	cur = con.cursor()
	cur.execute('SELECT * FROM myapp_card')
	collection = cur.fetchall()
	print(collection[0])
	'''
	cards = card.objects.all()
	return render(request, 'collection.html', {'cards' : cards})