from django.db import models
from django.contrib.auth.models import User
import random
import string

# Create your models here.
# models.py


class Prize(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='prizes/')
    value = models.CharField(max_length=100)  # You can use DecimalField for exact amounts
    details = models.TextField()  # Detailed description of the prize
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name








class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    tracking_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = self.generate_tracking_number()
            while Entry.objects.filter(tracking_number=self.tracking_number).exists():
                self.tracking_number = self.generate_tracking_number()
        super().save(*args, **kwargs)

    def generate_tracking_number(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

class AccountDetails(models.Model):
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    account_name = models.CharField(max_length=255)
    routing_number = models.CharField(max_length=20, blank=True, null=True)
    swift_code = models.CharField(max_length=20, blank=True, null=True)
    iban = models.CharField(max_length=34, blank=True, null=True)

    def __str__(self):
        return self.bank_name
