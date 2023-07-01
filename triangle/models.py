from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class LogEntry(models.Model):
    METHODS_CHOICES = [
        ('POST', 'post'),
        ('GET', 'get'),
        ('PUT', 'put'),
        ('PATCH', 'patch'),
        ('DELETE', 'delete'),
        ('HEAD', 'head'),
        ('OPTIONS', 'options'),
    ]
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10, choices=METHODS_CHOICES, default='GET')
    timestamp = models.DateTimeField(auto_now_add=True)
    request_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.method} {self.path}"
