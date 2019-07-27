from django.http import HttpResponse
from django.shortcuts import render

#metode viwes index
def index(request):
	return render (request, 'index.html')



def about (request):
	context = {
		'nav' : [
			['/', 'home'],
			['/profil', 'profil'],
			['/about', 'about'],
			['/contact', 'contact']
		]

	}
	return render (request, 'about.html',context)

def contact (request):
	context = {
		'nav' : [
			['/', 'home'],
			['/profil', 'profil'],
			['/about', 'about'],
			['/contact', 'contact']
		]

	}
	return render (request, 'contact.html', context)