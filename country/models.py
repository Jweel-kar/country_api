from django.db import models


# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100, unique=True)
    country_lang = models.CharField(max_length=100)
    country_currency = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    last_updated = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return self.country_name