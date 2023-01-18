from django.contrib import admin

# Register your models here.
from .models import Cosplay, CosEvent

admin.site.register(Cosplay)
admin.site.register(CosEvent)