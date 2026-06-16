from django.db import models

# Create your models here.
from django.db import models

class Donation(models.Model):
    donor_name = models.CharField(max_length=100)
    food_item = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[
        ('available', 'Available'),
        ('claimed', 'Claimed'),
        ('expired', 'Expired'),
    ], default='available')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor_name} - {self.food_item}"