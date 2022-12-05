from django.db import models

class Game(models.Model):
    title=models.CharField(max_length=255)
    year=models.CharField(max_length=255)
    factory_sealed=models.CharField(max_length=255)
    console=models.IntegerField(default=0)
    version=models.IntegerField(default=0)