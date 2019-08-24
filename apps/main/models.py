from __future__ import unicode_literals
from django.db import models

class Network(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 1:
            errors['title'] = "Enter a title"
        if len(postData['network']) < 1:
            errors['network'] = "Enter a network"
        if postData['releaseDate'] == "":
            errors['releaseDate'] = "Enter a release date"
        if len(postData['title']) > 120:
            errors['description'] = "Description must not exceed 120 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=False, null=True, blank=True)
    description = models.TextField()
    network = models.ForeignKey(Network, related_name="shows")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

