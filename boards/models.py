from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self): #is a string representation of a string
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated=models.DateTimeField(auto_now_add=True) #sets the exact time when post is upated
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name ='topics', on_delete=models.CASCADE)

class Post(models.Model):
    message = models.CharField(max_length=1000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)



