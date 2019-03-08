from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Event(models.Model):
    """
    A events can created by user
    This model links to the Django auth User model to manage access permissions.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    title = models.CharField(max_length=120, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date")
    participants = models.ManyToManyField(User, blank=True, verbose_name="Participants")

    def __str__(self):
        return str(self.title)
