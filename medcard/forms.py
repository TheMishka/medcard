from django import forms
from .models import Human, HumanDocument, PhoneNumber, PersonEmail

class NewPerson(forms.ModelForm):
        class Meta:
            model = Human
            exclude = ('create_date',)
            widgets = {
                'birthday': forms.DateInput(format=('%d.%m.%Y'))
            }
            labels = {
                'name': ('Имя'),
                'patronymic': ('Отчество'),
                'surname': ('Фамилия'),
                'birthday': ('Дата рождения'),
                'residence': ('Место жительства'),
                'gender': ('Пол'),
                'blood': ('Группа гкрови'),
                'rh': ('Резус')
            }

class Phone(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        exclude = ('human',)
        labels = {
            'phoneNumber': ('Номер телефона'),
            'phoneType': ('Тип')
        }

class Email(forms.ModelForm):
    class Meta:
        model = PersonEmail
        exclude = ('human',)
        labels = {
            'email': ('Электронная почта'),
            'emailType': ('Тип')
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