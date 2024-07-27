from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    '''
    This is class for to define posts for blog app

    '''
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=255)
    status = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name