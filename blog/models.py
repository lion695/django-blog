from django.db import models
from django.contrib.auth.models import User  # Import the User model

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True) #This is a string field
    slug = models.SlugField(max_length=200, unique=True)  #This is a string field
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') #This is a User Object instance (maps to an integer ID)
    content = models.TextField() #This is a string field
    created_on = models.DateTimeField(auto_now_add=True) #This is a datetime object field
    status = models.IntegerField(choices=STATUS, default=0) #This is an integer field

# Add your new field right here:
    updated_on = models.DateTimeField(auto_now=True)

    # Add your new optional summary field here:
    excerpt = models.TextField(blank=True, null=True)