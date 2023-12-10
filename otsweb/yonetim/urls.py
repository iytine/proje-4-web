from django.urls import path
from . import views

urlpatterns = [
    path('yonetim/', views.yonetim, name='yonetim'),
    path('yonet/', views.yonetim, name='yonetim'),
]
