from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='bookd'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu-item/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item'),
    path('booking/', views.BookingViewSet.as_view({'get': 'list'}), name='booking'),
    
    path('api-token-auth/', obtain_auth_token),
]