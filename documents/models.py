from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Document(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('done', 'Done'),
        ('failed', 'Failed'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    raw_text = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.owner.email})"

class Entity(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE,
                                 related_name='entities')
    text = models.CharField(max_length=255)
    label = models.CharField(max_length=100)
    start_char = models.IntegerField()
    end_char = models.IntegerField()

    def __str__(self):
        return f"{self.label}: {self.text}"