from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=80, blank=True)
  bio = models.TextField(max_length=254, blank=True)
  profile_pic = CloudinaryField('profile_pic/', default='profile_photos/user')
  location = models.CharField(max_length=50, blank=True, null=True)

  def __str__(self):
    return f'{self.user.username} Profile'
  
