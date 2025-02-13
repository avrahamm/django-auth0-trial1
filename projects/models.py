from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    founder = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)
    image = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.title} {self.technology}"
