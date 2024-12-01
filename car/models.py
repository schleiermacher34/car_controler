from django.db import models

class Command(models.Model):
    COMMAND_CHOICES = [
        ('auto', 'Auto'),
        ('manual', 'Manual'),
        ('forward', 'Forward'),
        ('backward', 'Backward'),
        ('left', 'Left'),
        ('right', 'Right'),
        ('stop', 'Stop'),
    ]
    command = models.CharField(max_length=10, choices=COMMAND_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    executed = models.BooleanField(default=False)

    def __str__(self):
        return self.command
