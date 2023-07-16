from django.shortcuts import render
from .models import Menu


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render()

def book(request):
    return render()
    
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def display_menu_item(request, pk):
    return render()


