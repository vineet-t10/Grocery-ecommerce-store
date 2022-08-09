from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    Like = models.ManyToManyField(User,related_name='like')
    price = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name