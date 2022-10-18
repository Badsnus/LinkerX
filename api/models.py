from django.db import models
from django.contrib.auth.admin import User


class Link(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=10, db_index=True, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class LinkFollow(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    device = models.CharField(max_length=300)
    follow_time = models.DateTimeField(auto_now_add=True)
