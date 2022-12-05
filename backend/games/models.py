from django.db import models

#Note charfields are adjusted for efficiency



class Game(models.Model):
    title=models.CharField(max_length=200, default="Only include title please")
    year=models.DateField()
    description=models.TextField(default="Include a description of condition and other relevant information...")
    factory_sealed=models.BooleanField(default=False)
    console=models.CharField(max_length=255)
    version=models.DecimalField(max_digits=10, decimal_places=8)

    def __str__(self):
        return self.title + ' - ' + self.description

