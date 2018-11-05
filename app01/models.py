from django.db import models

# Create your models here.

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,null=False,unique=True)
    def __str__(self):
        return "<Publisher Object:{}>".format(self.name)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,null=False,unique=True)
    publisher = models.ForeignKey(to='Publisher')

    def __str__(self):
        return "<Book Object:{}>".format(self.name)

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,null=False)
    book = models.ManyToManyField(to='Book')
    def __str__(self):
        return "<Autor Object:{}>".format(self.name)