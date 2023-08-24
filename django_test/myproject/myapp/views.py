from django.shortcuts import render, redirect
from django.db.models import Count
from datetime import date
from .forms import CardForm, SearchForm
from .models import card, CardManager, collection_table_entry, collection_table_entry, set_tracker_manager, set_tracker
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

				# Check if card exists in the collection already with the same set
				# if so, update the copies value, else create a new card

				if card.objects.filter(name=entry_dict['name'],setcode=entry_dict['setcode']):
					card_to_update = card.objects.get(name=entry_dict['name'],setcode=entry_dict['setcode'])
					card_to_update.copies = card_to_update.copies + entry_dict['copies']
					card_to_update.save()
					
					# increment the owned portion but not the unique or ratio

					tracker = set_tracker.objects.get(setcode=entry_dict['setcode'])
					tracker.owned = tracker.owned + entry_dict['copies']
					tracker.save()
					

				else:
					entry = card.objects.create(**entry_dict)
					entry.save()

				# Check if set exists in the collection already, card is unique
				# if so, update the set tracker with the new count information
				# else create a new set

					if set_tracker.objects.filter(setcode=entry_dict['setcode']):
						tracker = set_tracker.objects.get(setcode=entry_dict['setcode'])
						tracker.owned = tracker.owned + entry_dict['copies']
						tracker.unique = tracker.unique + 1
						tracker.ratio = str(tracker.unique) + '/' + str(tracker.total)
						tracker.save()
				
					else:
						con = sqlite3.connect("AllPrintings.sqlite")
						cur = con.cursor()

						print('SELECT baseSetSize FROM sets WHERE code = ' + entry_dict['setcode'].strip())
						print(entry_dict['setcode'])
						#query = 'SELECT baseSetSize FROM sets WHERE code = ' + entry_dict['setcode'.strip()]
						total_cards_in_set = cur.execute('SELECT baseSetSize FROM sets WHERE code = ?',(entry_dict['setcode'],)).fetchall()[0]
						ratio = "1/" + str(total_cards_in_set)

						tracker = set_tracker.objects.create(total=total_cards_in_set[0], owned=entry_dict['copies'], unique=1, ratio=ratio, setcode=entry_dict['setcode'])
						tracker.save()


			form = CardForm()

			return redirect('/myapp')

	context	= {'form':form}
	return render(request, "index.html", context)

def card_collection(request):

	context = {}
	rows = []
	sets_with_owned_cards = []
	con = sqlite3.connect("db.sqlite")
	cur = con.cursor()

	sets = set_tracker.objects.values().order_by('-unique')
	
	for s in sets:
		rows.append(s)
	context.update({'rows':rows})

	return render(request, 'collection/collection.html', context)
	

def collection_specific(request, setcode):
	
	cards = card.objects.filter(setcode=setcode)
	return render(request, 'collection/collection_specific.html', {'cards' : cards})

def search(request):
	form = SearchForm()
	if request.POST:
		form = SearchForm(request.POST)
		if form.is_valid():
			
			qvalues = []
			query = "SELECT * from myapp_card where"
			
			
			for item in form:
				
				qvalues.append(item.value())
			
			test = card.objects.filter(name__icontains=qvalues[0],setcode__icontains=qvalues[1],colors__icontains=qvalues[2],manaCost__icontains=qvalues[3],power__icontains=qvalues[4],
									toughness__icontains=qvalues[5],subtypes__icontains=qvalues[6],text__icontains=qvalues[7])

			return render(request, 'search_result.html', {'cards':test})

	context	= {'form':form}
	return render(request, 'search.html', context)