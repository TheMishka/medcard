from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone


class Human(models.Model):
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    residence = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('m', 'Мужской'),
        ('f', 'Женский')
        )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    create_date = models.DateTimeField(auto_now=True)
    blood = models.CharField(max_length=10)
    RH_CHOICES = (
        ('p', 'Положительный'),
        ('m', 'Отрицательный')
    )
    rh = models.CharField(max_length=1, choices=RH_CHOICES)

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

class PersonEmail(models.Model):
    human = models.ForeignKey(Human)
    email = models.EmailField()
    MAILTYPE_CHOICES = (
        ('p', 'Личный'),
        ('w', 'Рабочий'),
        ('o', 'Другой')
    )
    emailType = models.CharField(max_length=1, choices=MAILTYPE_CHOICES)


class DiagnosisCategory(MPTTModel):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class DiagnosisRelation(models.Model):
    human = models.ForeignKey(Human)
    diagnosis = models.ForeignKey(DiagnosisCategory)
    create_date = models.DateField(verbose_name='Дата постановки диагноза')
    change_date = models.DateTimeField(auto_now=True)

#class Anamnesis(models.Model):
    
