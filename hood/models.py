from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=80, blank=True)
  bio = models.TextField(max_length=254, blank=True)
  profile_pic = CloudinaryField('profile_pic/', default='profile_pic/user')
  location = models.CharField(max_length=50, blank=True, null=True)
  neighbourhood = models.ForeignKey('NeighbourHood', on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

  def __str__(self):
    return f'{self.user.username} Profile'

class NeighbourHood(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=60)
  admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
  hood_logo =  CloudinaryField('hood_pic/', default='profile_pic/user')
  description = models.TextField()
  health_tell = models.IntegerField(null=True, blank=True)
  health_officer = models.CharField(max_length=60, null=True, blank=True)
  police_tell = models.IntegerField(null=True, blank=True)
  police_officer = models.CharField(max_length=60, null=True, blank=True)

  def __str__(self):
    return f'{self.name} hood'
  
