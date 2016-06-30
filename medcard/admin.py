from django.contrib import admin

# Register your models here.

from .models import Human, HumanDocument

admin.site.register(Human)
admin.site.register(HumanDocument)
