from django.shortcuts import HttpResponse
from django.template import RequestContext


def index(request):
    return HttpResponse("Hello, world.", RequestContext(request))

