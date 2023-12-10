from django.http import HttpResponse
from django.template import loader

def anasayfa(request):
  template = loader.get_template('ana.html')
  return HttpResponse(template.render())
