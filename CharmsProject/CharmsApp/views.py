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

global score
score = 0

def button(request):
    return render(request, "index.html")

def external(request):
    inp = "/Users/Lorraine/Documents/AD19/Compiladores/Charms/Examples/test.txt"
    out = run([sys.executable, "//Users//Lorraine//Documents//AD19//Compiladores//Charms//CharmsRunner.py", inp], shell=False, stdout=PIPE)
    stdout = str(out.stdout)
    wasSuccessful= stdout.find('Success') != -1

    if wasSuccessful:
        return render(request, 'index.html', {'data1': getSuccessMessage(), 'scorep': addScore() })
    else:
        return render(request, 'index.html', {'data1': getErrorMessage(), 'scorep': score })

def getSuccessMessage():
    return "You've managed to perform the spell correctly. Thanks to you, your house has earned 200 points."

def getErrorMessage():
    return "It looks like you're missing something. Read the instructions and run your code again."

def addScore():
    global score
    score = score + 100
    return score
