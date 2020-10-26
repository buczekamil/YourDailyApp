from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50)
    if_done = models.BooleanField(default=False)
    to_date = models.DateField()
    time = models.TimeField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    add_to_calendar = models.BooleanField()
    user = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
