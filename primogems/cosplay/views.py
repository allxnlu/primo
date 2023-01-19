from django.shortcuts import render, get_object_or_404

from .models import Cosplay,CosEvent

# Create your views here.
def cosplay_detail(request, id):
    cosplay = get_object_or_404(Cosplay, pk=id)
    return render(request, "cosplay/cosplay_detail.html", {"cosplay":cosplay})

def event_list(request):
    return render(request, "events/event_list.html",
        {"events":CosEvent.objects.all()})

def event_detail(request, id):
    ebento = get_object_or_404(CosEvent, pk=id)
    return render(request, "events/event_detail.html", {"event":ebento})