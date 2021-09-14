from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    balance = models.IntegerField()

    def __str__(self):
        return f'[{self.pk}] {self.first_name}'
