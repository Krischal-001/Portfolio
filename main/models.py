from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='projects/',blank=True,null=True)
    
    def __str__(self):
        return self.title
    


class Contact(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)  # automatically sets submission time
    
    
class About(models.Model):
    title = models.CharField(max_length=100, default="About Me")
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
