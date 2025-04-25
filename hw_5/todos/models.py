from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
