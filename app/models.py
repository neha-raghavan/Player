from django.db import models

# Create your models here.
class People(models.Model):

    name = models.TextField(max_length=20)

    email = models.EmailField(max_length=254)
    country=models.TextField(max_length=20)
    game=models.TextField(max_length=20)
    score=models.IntegerField()


    def __str__(self):
        return self.name
