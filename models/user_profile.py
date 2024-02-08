from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Link to the Django built-in User model via OneToOneField for user profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Additional fields for user profile
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    # Optional: For enhanced functionality, consider adding fields like profile picture, etc.
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
