from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    COURSE_CHOICES = [('Python', 'Python'), ('Java', 'Java'), ('UI/UX', 'UI/UX')]
    FEES_CHOICES = [('Yes', 'Yes'), ('No', 'No')]

    roll_number = models.CharField(max_length=20)
    name = models.CharField(max_length=30) 
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    enroll_course = models.CharField(max_length=30, choices=COURSE_CHOICES)
    contact = models.CharField(max_length=30)
    education = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    parent_name = models.CharField(max_length=30)
    Dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    fees_paid = models.CharField(max_length=10, choices=FEES_CHOICES, default='No')
    date_of_joining = models.DateField(blank=True, null=True, verbose_name="Joining Date")
    image = models.ImageField(upload_to="students/", blank=True, null=True)

    def __str__(self):
        return self.name
