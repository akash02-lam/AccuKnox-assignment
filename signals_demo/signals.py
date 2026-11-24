from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event, AuditLog


# Question 1: Create a custom signal
question1_signal = Signal()


@receiver(question1_signal)
def question1_receiver(sender, **kwargs):
    print("Q1: Receiver started")
    print("Q1: Receiver finished")


import threading

# Question 2: Create another custom signal
question2_signal = Signal()


@receiver(question2_signal)
def question2_receiver(sender, **kwargs):
    receiver_thread = threading.get_ident()

    print("Q2: Receiver thread ID:", receiver_thread)


@receiver(post_save, sender=Event)
def create_audit_log(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            event=instance,
            message="Event created"
        )
        print("Q3: Audit log created")

