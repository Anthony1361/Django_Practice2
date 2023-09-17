from django.db import models

# Create your models here.
class ourBlog(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="img", null= True, blank= True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
