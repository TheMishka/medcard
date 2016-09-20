from django import forms
from .models import Human, HumanDocument

class NewPerson(forms.ModelForm):
        class Meta:
            model = Human
            exclude = ('create_date',)
            labels = {
                'name': ('Имя'),
                'surname': ('Фамилия'),
                'birthday': ('Дата рождения'),
                'place_of_birth': ('Место рождения'),
                'gender': ('Пол'),
                'age': ('Возраст'),
                'inn': ('ИНН')
            }
            error_messages = {
                'age': {
                    'max_length': ("Столько не живут!"),
                },
            }

class DocumentEdit(forms.ModelForm):
        class Meta:
            model = HumanDocument
            exclude = ('human',)
#            fields = '__all__'
#            widgets = {'human': forms.HiddenInput()}
            labels = {
                'document_type': ('Тип документа'),
                'document_number': ('Номер документа'),
                'document_date': ('Дата выдачи документа')
            }