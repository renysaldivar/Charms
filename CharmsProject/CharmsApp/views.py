from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

def index(request):
    return HttpResponse("Test")
