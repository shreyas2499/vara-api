from django.db import models


# Create your models here.

class User(models.Model):  # Viewed by User
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.TextField(null=False)
    preferences = models.JSONField()


class MonthlyConsumption(models.Model):
    field = models.CharField(max_length=20)
    jan = models.FloatField()
    feb = models.FloatField()
    march = models.FloatField()
    april = models.FloatField()
    may = models.FloatField()
    june = models.FloatField()
    july = models.FloatField()
    august = models.FloatField()
    sept = models.FloatField()
    oct = models.FloatField()
    nov = models.FloatField()
    dec = models.FloatField()

# password: nyutandon