from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    
    SKILL_CHOICES =[
        ('', 'CHOOSE SKILL'),
        ('teacher', 'Teacher'), ('musician', 'Musician')
    ]

    skill = models.CharField(max_length=100, choices=SKILL_CHOICES)
    
    profile_picture = models.ImageField(upload_to="profile_pic", default= "default.jpg" ,null=True, blank=True)

    def __str__(self):
         return self.first_name
