from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='bookd'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu_item/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu_item'),
]