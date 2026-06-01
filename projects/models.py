from django.db import models
from django.contrib.auth.models import User
# Create your models (Entities) here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    # The __str__ method tells Django how to display
    # this object in plain text whenever a human needs to see it.

    def __str__(self):
        return self.name

class ProjectStatus(models.IntegerChoices):
    PENDING = 1,'Pending'
    COMPLETED = 2,'Completed'
    POSTPONED = 3,'Postponed'
    CANCELED = 4,'Canceled'




class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(choices=ProjectStatus.choices, default=ProjectStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #realtionship OneToMany
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null =True )#CASCADE:It tells Django what should happen to the projects if the owner's user account is completely deleted.

    def __str__(self):
        return self.title

class Tasks(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)#just added so not completed
    project =models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

