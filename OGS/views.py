from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from OGS.models import Organization,GoodsServices


def index(request):
    args = {}
    args.update(csrf(request))
    args['Organization'] = Organization.objects.get(id=1)
    args['Service'] = GoodsServices.objects.get(id=1)
    args['test'] = Organization.objects.get(name="Пегас")
    return render_to_response('OGS/index.html', args)
