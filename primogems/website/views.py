from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from cosplay.models import CosEvent, Cosplay
# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html",
        {"norem":"What if I told you that I've fallen, and I like the way you say my name~",
        "curr_event": CosEvent.objects.all()[1],
        "image": Cosplay.objects.all()[1].no_images})

def date(request):
    return HttpResponse("Current time: " + str(datetime.now()))

def about(request):
    return HttpResponse("Hi im lyn from las vegas models")