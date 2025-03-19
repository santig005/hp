from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    pokemon_id = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    types = models.CharField(max_length=200)

    def __str__(self):
        return self.name