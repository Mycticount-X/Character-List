from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    hp = models.IntegerField(default=100)
    atk = models.IntegerField(default=10)
    defense = models.IntegerField(default=5)
    spd = models.IntegerField(default=10)
    stm = models.IntegerField(default=50)
    mtx = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.name} [Level: {self.level}]"