from django.dispatch import Signal, receiver

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
