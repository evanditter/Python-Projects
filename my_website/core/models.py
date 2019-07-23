from django.db import models
from datetime import datetime

# Create your models here.

class Core(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        verbose_name_plural = "Core"
