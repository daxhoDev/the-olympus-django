from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Profile(AbstractUser):
    
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=20, choices=[('user', 'User'), ('admin', 'Admin')], default='user')
    deleted_at = models.DateTimeField(null=True, blank=True)
    bank_account = models.CharField(max_length=30, null=False, blank=False)
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = 'admin'
        super().save(*args, **kwargs)

class Plan(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    features = models.JSONField(default=list)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} | ${self.price}'
    
class Payment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment of ${self.amount} by {self.profile.username} on {self.date}'
    
class Invitation(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=20, choices=[('user', 'User'), ('admin', 'Admin')], default='user')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Invitation to {self.email}'
    
    def save(self, *args, **kwargs):
        if not self.token:
            self.token = str(uuid.uuid4())
        super().save(*args, **kwargs)