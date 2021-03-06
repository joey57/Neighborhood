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

  def create_neighborhood(self):
    self.save()

  def delete_neighborhood(self):
    self.delete()

  def save_neighborhood(self):
    self.save()  

  @classmethod
  def find_neighborhood(cls, neighborhood_id):
    return cls.objects.filter(id=neighborhood_id)

class Business(models.Model):
  name = models.CharField(max_length=120)
  email = models.EmailField(max_length=254)
  description = models.TextField(blank=True)
  neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='business')
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')

  def __str__(self):
    return f'{self.name} Business'

  def create_business(self):
    self.save()

  def delete_business(self):
    self.delete()

  def save_business(self):
    self.save()  

  @classmethod
  def search_business(cls, name):
    return cls.objects.filter(name__icontains=name).all() 

class Post(models.Model):
  title = models.CharField(max_length=120, null=True)
  post = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
  hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='hood_post')
  
