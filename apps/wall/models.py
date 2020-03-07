from django.db import models

class Message(models.Model):
    message=models.TextField()
    poster=models.ForeignKey('app1.User', related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.TextField()
    poster=models.ForeignKey('app1.User', related_name="comments")
    message=models.ForeignKey(Message, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)