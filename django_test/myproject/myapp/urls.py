from django.urls import path
from . import views

urlpatterns = [
	path('', views.myview),
	path('collection', views.card_collection),
	path('collection_specific/<setcode>/', views.collection_specific),
	path('search', views.search)
	]