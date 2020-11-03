from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, editable=False, null=True, on_delete=models.CASCADE)
