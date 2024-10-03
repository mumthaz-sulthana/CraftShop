from django.db import models

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    
    bio = models.CharField(max_length=200, null=True)
    
    profile_pic = models.ImageField(upload_to="profile_pictures", default="/profile_pictures/default.png")
    
    user_object = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    updated_date = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_object.username
    
class Category(models.Model):
    
    title = models.CharField(max_length=200, unique=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    updated_date = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    
    name = models.CharField(max_length=200)
    
    description = models.TextField()
    
    category_object = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    price = models.PositiveIntegerField()
    
    stock = models.IntegerField()
    
    image = models.ImageField(upload_to='products/')
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    updated_date = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
