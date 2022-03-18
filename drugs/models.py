from django.db import models

# Class for drug active ingredient.
class ActiveIng(models.Model):
    name = models.CharField(max_length=150, unique=True)
    dose = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return self.name

class Drug(models.Model):
    name = models.CharField(max_length=150)
    active_ing = models.ForeignKey(ActiveIng, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.name
