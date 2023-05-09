from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=50)


class Message(models.Model):
    text = models.TextField()
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)