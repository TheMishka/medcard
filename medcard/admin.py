from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
# Register your models here.

from .models import Human, HumanDocument, PhoneNumber, Email, DiagnosisCategory, DiagnosisRelation

class DiagnosisAdmin(DjangoMpttAdmin):
    tree_auto_open = 0
    list_display = ('code', 'name',)
    ordering = ('code',)

admin.site.register(Human)
admin.site.register(HumanDocument)
admin.site.register(PhoneNumber)
admin.site.register(Email)
admin.site.register(DiagnosisCategory, DiagnosisAdmin)
admin.site.register(DiagnosisRelation)