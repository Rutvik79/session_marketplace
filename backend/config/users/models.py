from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('USER', 'User'),
        ('CREATOR', 'Creator'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='USER'
    )

    avatar = models.URLField(
        blank=True,
        null=True,
        help_text="Profile image URL"
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
