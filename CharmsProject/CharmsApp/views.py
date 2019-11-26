from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader
import requests
from subprocess import run, PIPE
import sys

# def index(request):
#     template = loader.get_template('index.html')
#     context = {}
#     index = template.render(context, request)
#     return HttpResponse(index)

def button(request):
    return render(request, "home.html")

def external(request):
    inp = request.POST.get('param')
    out = run([sys.executable, "//Users//Lorraine//Documents//AD19//Compiladores//Charms//test.py", inp], shell=False, stdout=PIPE)
    print(out)

    return render(request, 'home.html', {'data1': out})