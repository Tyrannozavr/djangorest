from django.db import models
from authentication.models import User

class Tickets(models.Model):
    choices = (
        ('unsolved', 'unsolved'),
        ('solved', 'solved'),
        ('freezed', 'freezed'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tikets')
    status = models.CharField(max_length=20, choices=choices)

    def __str__(self):
        return f'id: {self.id} user: {self.user.username} status: {self.status}'

class Message(models.Model):
    message = models.TextField(max_length=1000)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='messages')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message')

    def __str__(self):
        return f'owner: {self.owner} message: {self.message}'
