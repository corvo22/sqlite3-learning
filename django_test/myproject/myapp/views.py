from django.shortcuts import render, redirect
from django.db.models import Count
from datetime import date
from .forms import CardForm
from .models import card, CardManager, collection_table_entry, collection_table_entry
import sqlite3, re

# Create your views here.
def myview(request):
	form = CardForm()
	if request.POST:
		form = CardForm(request.POST)
		if form.is_valid():

			qset = (form['name'].value(), form['setCode'].value().upper(), form['setNumber'].value())

			con = sqlite3.connect("AllPrintings.sqlite")
			cur = con.cursor()
			
			entry_keys = ['name','artist','colors','power','toughness','manaValue','manaCost','text','setcode','subtypes','supertypes','types','setNumber','copies']
			entry_values = cur.execute("SELECT name,artist,colors,power,toughness,manaValue,manaCost,text,setcode,subtypes,supertypes,types,number FROM cards WHERE name = ? AND setCode = ? AND number = ?",qset).fetchall()
			
			if entry_values:
				entry_values = list(entry_values[0])

				entry_values.append(int(form['copies'].value()))

				entry_dict = dict(zip(entry_keys,entry_values))
				entry_dict['text'] = re.sub("\\\\n"," ",entry_dict['text'])

				# Check if card exists in the collection already

				if card.objects.filter(name=entry_dict['name']):
					card_to_update = card.objects.filter(name=entry_dict['name'])
					count = card_to_update.update(copies=card_to_update.values('copies'))
					card_to_update.update(copies = (count + 1)) 

				else:
					entry = card.objects.create(**entry_dict)
					entry.save()

			form = CardForm()

			return redirect('/myapp')

	context	= {'form':form}
	return render(request, "index.html", context)

def card_collection(request):

	context = {}
	rows = []
	sets_with_owned_cards = []
	con = sqlite3.connect("AllPrintings.sqlite")
	cur = con.cursor()



	owned_cards_in_set = card.objects.values('setcode').order_by('setcode').annotate(count=Count('setcode'))
	
	# build query string
	query = 'SELECT baseSetSize FROM sets WHERE '
	for s in owned_cards_in_set:
		setcode = s['setcode']
		query = query + 'code = "' + setcode + '" OR ' 
	
	query = query[:-4]
	total_cards_in_set = cur.execute(query).fetchall()
	
	# convert list of dictionary to context dictionary 
	i = 0
	for c in owned_cards_in_set:
		setcode = c['setcode']
		count = c['count']
		total = total_cards_in_set[i][0]
		ratio = str(count) + '/' + str(total)

		rows.append(collection_table_entry.objects.create(setcode = setcode,count = count, total = total, ratio = ratio))
		i += 1
	#print(rows)
	context.update({'rows':rows})

	print(context)
	
	return render(request, 'collection/collection.html', context)

def collection_specific(request, setcode):
	
	context = {}
	cards = card.objects.filter(setcode=setcode)
	return render(request, 'collection/collection_specific.html', {'cards' : cards})