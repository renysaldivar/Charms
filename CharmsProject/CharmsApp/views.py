from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    context = {}
    index = template.render(context, request)
    return HttpResponse(index)
