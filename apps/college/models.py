from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class College(models.Model):
    TIPO_CHOICES = [
        ('publica', 'Pública'),
        ('federal', 'Federal'),
        ('privada', 'Privada'),
    ]

    name = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
    def published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

class Campus(models.Model):
    college = models.ForeignKey(College,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def campus_college(self):
        return self.college


