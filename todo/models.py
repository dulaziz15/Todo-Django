from email.policy import default
from enum import auto
from random import choices
from secrets import choice
from tkinter.tix import Tree
from unittest.util import _MAX_LENGTH
from venv import create
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
class Task(models.Model):
    class TaskStatus(models.TextChoices):
        TODO = "todo", _ ('Closed')
        IN_PROGRES = 'in_progress', _ ('in_progres')
        CLOSED = 'closed', _ ('Closed')

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length = 20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'