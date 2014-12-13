from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf


def index(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('OGS/index.html', args)
