from django.db import models
from django.utils import timezone


class Human(models.Model):
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('m', 'Мужской'),
        ('f', 'Женский')
        )
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HumanDocument(models.Model):
    human = models.ForeignKey(Human)
    document_type = models.CharField(max_length=20)
    document_number = models.PositiveIntegerField()
    document_date = models.DateField()

    def __str__(self):
        return self.document_type

class PhoneNumber(models.Model):
    human = models.ForeignKey(Human)
    phoneNumber = models.CharField(max_length=20)
    PHONETYPE_CHOICES = (
        ('m', 'Сотовый'),
        ('w', 'Рабочий'),
        ('o', 'Другой')
    )
    phoneType = models.CharField(max_length=1, choices=PHONETYPE_CHOICES)

class Email(models.Model):
    human = models.ForeignKey(Human)
    email = models.EmailField()
    MAILTYPE_CHOICES = (
        ('p', 'Личный'),
        ('w', 'Рабочий'),
        ('o', 'Другой')
    )
    emailType = models.CharField(max_length=1, choices=MAILTYPE_CHOICES)


# class Diagnosis(models.Model):

#class Anamnesis(models.Model):
    
