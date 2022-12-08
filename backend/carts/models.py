from django.db import models
from authentication.models import User
from games.models import Game

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    game=models.ForeignKey(Game, on_delete=models.CASCADE)
    payment_processed=models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ': ' + self.game.title + ' - ' + self.game.description
        #Allows fields to show up in when running django web application