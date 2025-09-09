from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
        User profile model extending Django's built-in User model.

        Stores additional information about users beyond the default User model.
        Each user can have only one profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
