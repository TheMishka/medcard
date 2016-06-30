from django.db import models
from django.utils import timezone


class Human(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('m', 'Мужской'),
        ('f', 'Женский')
        )
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES)   
    age = models.PositiveIntegerField()
    inn = models.PositiveIntegerField()
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

class HumanDocument(models.Model):
    human = models.ForeignKey(Human)
    document_type = models.CharField(max_length=20)
    document_number = models.PositiveIntegerField()
    document_date = models.DateField()

    def __str__(self):
        return self.document_type


    
    
