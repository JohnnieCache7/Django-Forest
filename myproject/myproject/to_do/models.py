from django.db import models


# Create your models here.
class to_do_item(models.Model):
    who_added = models.CharField(
        max_length=200
    )  # who_added - Person who added the chore
    who_assigned = models.CharField(
        max_length=200
    )  # who_assigned - Person who is supposed to complete the work
    add_date = models.DateTimeField(
        "created date"
    )  # add_date - When the task was added to the system
    to_do_name = models.CharField(
        max_length=500
    )  # to_do_name - Description of the task
    due_date = models.DateTimeField(
        "due date"
    )  # due_date - When the task needs to be completed
    completed = models.IntegerField(default=0)  # completed - 0 for not done, 1 for done
