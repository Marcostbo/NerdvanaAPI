from django.db import models
from nerdvanapp.models import User, Games


class PriceAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8, null=False)
    created_on = models.DateTimeField(null=True, blank=True)
    resolved_on = models.DateTimeField(null=True, blank=True)
    is_resolved = models.BooleanField(default=False)
    price_resolved = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    link_resolved = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = 'Price alert'
        verbose_name_plural = 'Price alerts'

    def __str__(self):
        return f'Alert for {self.game.name} with price R${self.price} to {self.user.email}'
