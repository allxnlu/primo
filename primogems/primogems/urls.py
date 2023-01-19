from django.contrib import admin
from django.urls import path
from website.views import welcome, date, about
from cosplay.views import cosplay_detail, event_list, event_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('date',date),
    path('about', about),
    path('cosplay/<int:id>', cosplay_detail, name='cosplay_detail'),
    path('event_list', event_list, name='event_list'),
    path('events/<int:id>', event_detail, name='event_detail')
]
