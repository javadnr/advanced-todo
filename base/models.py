from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User





class PostModel(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True, blank=True)
    created =models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField(default = False)
    
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):    
        return reverse("post_detail", args=[str(self.id)])



class Profile(models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null = True, blank=True,default='default.jpg',upload_to="images" )
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField( max_length=254)
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=50)
    perfession = models.CharField(max_length = 150,null=True,blank=True)
    twitter = models.URLField(max_length = 200,blank=True, null=True)
    instagram = models.URLField(max_length = 200,blank=True, null=True)
    github = models.URLField(max_length = 200,blank=True, null=True)

    
    
    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += " " + str(self.last_name)
        return name
    
    def get_absolute_url(self):    
        return reverse("profile", args=[str(self.id)])
    
