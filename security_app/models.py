from django.db import models
from django.contrib.auth.models import User

class System(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Atack(models.Model):
    system = models.ForeignKey(System,unique=False, on_delete=models.CASCADE, related_name='atacks')
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.title}"

class Copyright(models.Model):
    system = models.ForeignKey(System,unique=False, on_delete=models.CASCADE, related_name='copyright')
    watermark = models.ImageField(upload_to='watermarks/')
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.author} - {self.title} ({self.year})"

class SecurityEvent(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=255)
    description = models.TextField()
    occurred_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.system.name} - {self.event_type}"

class AccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    system = models.ForeignKey(System, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.action}"
