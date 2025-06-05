from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    
    image =models.ImageField(upload_to="teachers/", blank=True, null=True)  # admin USERNANE
                                                                        


def __str__(self):
    return(f"{self.name}-{self.subject}")




















