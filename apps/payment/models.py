# Create your models here.
from django.db import models

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    cash = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    upi = models.CharField(max_length=255, null=True, blank=True)
    online = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    booking_price = models.DecimalField(max_digits=10, decimal_places=2)
    status_choices = [
        ('Pending', 'Pending'),
        ('Successful', 'Successful'),
        ('Failed', 'Failed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Payment #{self.id} - {self.booking}'
