from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=20, choices=[('user', 'User'), ('admin', 'Admin')], default='member')
    
    def __str__(self):
        return self.username
    
    @property
    def is_admin(self):
        return self.is_staff or self.is_superuser

class Plan(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    features = models.JSONField(default=list)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} | ${self.price}'