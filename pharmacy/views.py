from django.shortcuts import render

def index(request):
    return render(request, 'pharmacy/index.html')

def about(request):
    return render(request, 'pharmacy/about.html')

def contacts(request):
    return render(request, 'pharmacy/contacts.html')

def how_to_find(request):
    return render(request, 'pharmacy/find.html')

def catalog(request):
    return render(request, 'pharmacy/catalog.html')

def promotions(request):
    return render(request, 'pharmacy/promotions.html')