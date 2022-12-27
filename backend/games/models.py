from django.db import models
from authentication.models import User

#Note charfields are adjusted for efficiency



class Game(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200, default="Only include title please")
    description=models.TextField(default="Include a description of condition and other relevant information...")
    cost=models.DecimalField(max_digits=6, decimal_places=2)
    year=models.DateField()
    factory_sealed=models.BooleanField(default=False)
    console=models.CharField(max_length=255)
    version=models.DecimalField(max_digits=10, decimal_places=8)
    image1 = models.ImageField(null=True, blank=True, upload_to="images/")
    image2 = models.ImageField(null=True, blank=True, upload_to="images/")
    image3 = models.ImageField(null=True, blank=True, upload_to="images/")
    image4 = models.ImageField(null=True, blank=True, upload_to="images/")
    image5 = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title + ' - ' + self.description
        #Allows fields to show up in when running django web application