from django.db import models



# Create your models here.


class Staff(models.Model):
    GENDER_CHOICES =[('male' 'male'), ('female','female')]
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    position = models.CharField(max_length=30)
    Experience = models.CharField(max_length=30)
    date_of_joining = models.DateField(blank=True, null=True)
    contact = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    
    image = models.ImageField(upload_to="staff/", blank=True, null=True)  
                                                                        


def __str__(self):
    return(f"{self.name}-{self.subject}")




















