from django.http import HttpResponse
from django.template import loader

def ogrenci(request):
  template = loader.get_template('abc.html')
  return HttpResponse(template.render())

from .models import Ogrenci

def ogrenciler(request):
    ogrenciliste = Ogrenci.objects.all()
    template = loader.get_template('ogrencilistesi.html')
    context ={
        'ogrenciliste' : ogrenciliste,
    }
    return HttpResponse(template.render(context, request))