from django.db import models

class Restaurant (models.Model):
    name = models.CharField(max_length=120);
    description = models.TextField()
    opening_time = models.DateField(auto_now_add=True)
    closing_time = models.DateField(auto_now_add=True)

def __str__ (self):
    return self.title
