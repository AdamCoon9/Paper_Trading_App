from django.db import models
from django.contrib.auth.models import User
from Project4_App_level.Project4_App_level.models import Stock
class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Trade(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts_trades')
        stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
        shares = models.IntegerField()
        price = models.DecimalField(max_digits=10, decimal_places=2)

        def __str__(self):
            return f'{self.user.username} - {self.stock.name}'
