from django.db import models

# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=100, blank=True)
    document = models.FileField(upload_to='document/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
