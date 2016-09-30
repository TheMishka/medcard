from django.contrib import admin

# Register your models here.

from .models import Human, HumanDocument, PhoneNumber, Email

admin.site.register(Human)
admin.site.register(HumanDocument)
admin.site.register(PhoneNumber)
admin.site.register(Email)