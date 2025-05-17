from django.db import models


class ConsultationRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
