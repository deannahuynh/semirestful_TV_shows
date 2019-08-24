from django.db import models

class Network(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Show(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=False, null=True, blank=True)
    description = models.TextField()
    network = models.ForeignKey(Network, related_name="shows")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

