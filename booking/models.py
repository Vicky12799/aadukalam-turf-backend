# Create your models here.
from django.db import models
from customer.models import Customer  # Import the Customer model
from manager.models import Manager  # Import the Manager model
from payment.models import Payment # Import the Payment model


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE)
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status_choices = [
        ('Booked', 'Booked'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Booked')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.ForeignKey('Payment', on_delete=models.CASCADE)  # Assuming you have a Payment model

    def __str__(self):
        return f'Booking #{self.id} - {self.cust_id.name}'