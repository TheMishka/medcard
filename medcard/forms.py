from django import forms
from .models import Human, HumanDocument

class NewPerson(forms.ModelForm):
        class Meta:
            model = Human
            exclude = ('create_date',)
            labels = {
                'name': ('Имя'),
                'patronymic': ('Отчество'),
                'surname': ('Фамилия'),
                'birthday': ('Дата рождения'),
                'place_of_birth': ('Место рождения'),
                'gender': ('Пол')
            }


class DocumentEdit(forms.ModelForm):
        class Meta:
            model = HumanDocument
            exclude = ('human',)
#            fields = '__all__'
            widgets = {
                'document_date': forms.DateInput(format=('%d.%m.%Y'))
            }
            labels = {
                'document_type': ('Тип документа'),
                'document_number': ('Номер документа'),
                'document_date': ('Дата выдачи документа')
            }