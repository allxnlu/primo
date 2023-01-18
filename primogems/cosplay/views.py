from django.shortcuts import render, get_object_or_404

from .models import Cosplay

# Create your views here.
def detail(request, id):
    cosplay = get_object_or_404(Cosplay, pk=id)
    return render(request, "cosplay/detail.html", {"cosplay":cosplay})