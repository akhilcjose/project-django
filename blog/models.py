from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title