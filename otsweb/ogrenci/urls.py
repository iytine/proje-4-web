from django.urls import path
from . import views

urlpatterns = [
    path('ogrenci/', views.ogrenci, name='ogrenci'),
    path('ogrenci1/', views.ogrenci, name='ana'), 
    path('ogrenciliste/', views.ogrenciler, name='ogrenci'),
]
