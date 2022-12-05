from django.db import models

class Game(models.Model):
    title=models.CharField(max_length=200)
    year=models.DateField()
    factory_sealed=models.CharField(max_length=255)
    console=models.CharField(max_length=255)
    version=models.IntegerField(default=0)