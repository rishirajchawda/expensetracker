from django.contrib.auth.models import User
from django.db import models


# Create your models here.
CHOOSE=(
    ('Credit','Credit'),
    ('Debit','Debit'),
)

class Profile(models.Model):
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    user_income = models.FloatField()
    expenses = models.FloatField(default=0)
    user_balance = models.FloatField()




class Expense(models.Model):
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    amount = models.FloatField()
    expense_type=models.CharField(max_length=100 , choices=CHOOSE)

    def __str__(self):
        return self.name
