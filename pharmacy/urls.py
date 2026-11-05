from django.urls import path
from . import views

app_name = 'pharmacy'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about/contacts/', views.contacts, name='contacts'),
    path('about/find/', views.how_to_find, name='find'),
    path('catalog/', views.catalog, name='catalog'),
    path('promotions/', views.promotions, name='promotions'),
]