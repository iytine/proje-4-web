from django.http import HttpResponse
from django.template import loader

def yonetim(request):
  template = loader.get_template('anay.html')
  return HttpResponse(template.render())


# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse

# def yonetim(request):
#     return HttpResponse("Yöntim bölümü")
