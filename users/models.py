from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def suspend(self):
        self.is_suspended = True
        self.save()

    def reactivate(self):
        self.is_suspended = False
        self.save()
