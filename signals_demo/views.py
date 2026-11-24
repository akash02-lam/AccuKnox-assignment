from django.shortcuts import render
from django.http import HttpResponse
from .signals import question1_signal
from .signals import question2_signal
from django.db import transaction
from .models import Event, AuditLog

def question1_view(request):
    print("Q1: Before signal")

    question1_signal.send(sender=None)

    print("Q1: After signal")

    return HttpResponse("Question 1 completed")


import threading


def question2_view(request):
    caller_thread = threading.get_ident()

    print("Q2: Caller thread ID:", caller_thread)

    question2_signal.send(sender=None)

    return HttpResponse("Question 2 completed")



def question3_view(request):

    try:
        with transaction.atomic():

            event = Event.objects.create(
                name="Django Test Event"
            )

            print("Q3: Event created")

            print(
                "Q3: Audit logs inside transaction:",
                AuditLog.objects.count()
            )

            # Force rollback to test the transaction
            raise Exception("Testing rollback")

    except Exception:
        print("Q3: Transaction rolled back")

    print(
        "Q3: Events remaining:",
        Event.objects.count()
    )

    print(
        "Q3: Audit logs remaining:",
        AuditLog.objects.count()
    )

    return HttpResponse("Question 3 completed")
