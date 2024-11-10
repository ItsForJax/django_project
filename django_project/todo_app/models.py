from django.db import models
from django.utils import timezone

# Create your models here.

class Todos(models.Model):
    title = models.CharField(max_length=200, null=False)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    date_completed = models.DateTimeField(null=True, blank = True)

    def save(self, *args, **kwargs):
        # Automatically set date_accomplished when the task is completed
        if self.completed and not self.date_completed:
            self.date_completed = timezone.now()  # Set the current time
        elif not self.completed:
            self.date_completed = None  # Clear the date when not completed
        super().save(*args, **kwargs)