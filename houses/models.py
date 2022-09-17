from django.db import models


class House(models.Model):

    """House Definition for Houses"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField()

    def __str__(self) -> str:
        return self.name
