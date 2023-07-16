from django.shortcuts import render
from .models import Menu, Booking
from rest_framework import generics, viewsets, permissions
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

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

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer