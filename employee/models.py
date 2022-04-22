from django.db import models

# Create your models here.
class Poste(models.Model):
    posteId = models.AutoField(primary_key=True)
    posteDesignation = models.CharField(max_length=100)

class Employe(models.Model):
    employeId = models.AutoField(primary_key=True)
    employeNom = models.CharField(max_length=100)
    employePostom = models.CharField(max_length=100)
    employePrenom = models.CharField(max_length=100)
    employeSexe = models.CharField(max_length=100)
    employeAdress = models.TextField()
    poste = models.ForeignKey(Poste, on_delete = models.CASCADE)
