from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.sender}: {self.content}"
