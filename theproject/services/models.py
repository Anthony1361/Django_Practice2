from django.db import models

# Create your models here.

class ourServices(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.name
