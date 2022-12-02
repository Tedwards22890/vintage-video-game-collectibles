from django.db import models
from authentication.models import User

class Cart(models.Model):
    user=models.ForeignKay(User, on_delete=models.CASCADE)
    game
    payment_processed=models.BooleanField(default=False)
