from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AuditLog(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message
