# AccuKnox Django Trainee Assignment

## Project Overview

This project was created as part of the AccuKnox Django Trainee technical assignment. It covers three questions related to Django Signals and one practical task based on Python classes and iterators.

The main purpose of this assignment was to understand how Django Signals work, how they interact with threads and database transactions, and how to make a custom Python class iterable.

## Technologies Used

- Python
- Django
- SQLite
- Git and GitHub

# Part 1: Django Signals

## What are Django Signals?

Django Signals allow different parts of an application to communicate with each other. They automatically execute a function when a particular event occurs.

For example, when a new user is created, a signal can automatically create a user profile or perform another task.

In simple terms, signals help us perform actions automatically when something happens in a Django application.

## Question 1: Are Django Signals synchronous or asynchronous by default?

**Answer:** Django Signals are synchronous by default when using synchronous receivers.

**Description:**

When a signal is sent, its receiver function executes immediately. The main program waits for the receiver to finish before moving to the next statement.

**Implementation:**

I created a custom signal and connected it to a receiver function. I used `send()` to trigger the signal and printed messages before and after sending it.

**Expected Output:**

```text
Q1: Before signal
Q1: Receiver started
Q1: Receiver finished
Q1: After signal
```

**Conclusion:**

The output shows that the receiver finishes its execution before the caller moves to the next statement. This demonstrates that synchronous signals execute in order.

## Question 2: Do Django Signals run in the same thread as the caller?

**Answer:** Yes, synchronous Django Signal receivers normally run in the same thread as the caller.

**Description:**

To check this, I used Python's `threading.get_ident()` function. It returns the ID of the current thread.

I printed the thread ID from both the caller function and the signal receiver, then compared the results.

**Expected Output:**

```text
Q2: Caller thread ID: 123456
Q2: Receiver thread ID: 123456
```

**Note:** The actual thread IDs may vary each time the project runs.

**Conclusion:**

Both thread IDs are identical, which shows that the synchronous signal receiver runs in the same thread as the caller.

## Question 3: Do Django Signals run in the same database transaction as the caller by default?

**Answer:** Yes, when the caller is already inside an active database transaction and both operations use the same database connection.

**Description:**

To demonstrate this, I used Django's `transaction.atomic()` to create a database transaction.

I created an Event model and an AuditLog model. When a new Event is created, the `post_save` signal automatically creates an AuditLog record.

After that, I deliberately raised an exception to test whether both database operations would be rolled back.

**Expected Output:**

```text
Q3: Audit log created
Q3: Event created
Q3: Audit logs inside transaction: 1
Q3: Transaction rolled back
Q3: Events remaining: 0
Q3: Audit logs remaining: 0
```

**Conclusion:**

Both the Event and AuditLog records were rolled back after the exception. This shows that the database operation performed by the signal receiver participated in the caller's active transaction.

# Part 2: Custom Classes in Python

## Task: Create a Rectangle Class

**Requirements:**

1. Create a Rectangle class that accepts two integer arguments: length and width.
2. Make the Rectangle object iterable.
3. When iterated, it should return two dictionaries in the following order:
   - First: `{'length': value}`
   - Second: `{'width': value}`

**Implementation:**

I created a Rectangle class with an `__init__()` method to initialize the length and width.

I used the `__iter__()` method with `yield` to make the object iterable. It returns the length and width as separate dictionaries, one at a time.

**Example:**

```python
rectangle = Rectangle(10, 5)

for item in rectangle:
    print(item)
```

**Expected Output:**

```text
{'length': 10}
{'width': 5}
```

**Conclusion:**

The Rectangle object can be used in a for loop and returns the required dictionaries in the correct order.

# Project Structure

```text
accuknox-django-trainee-assignment/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── signals_demo/
│   ├── migrations/
│   ├── apps.py
│   ├── models.py
│   ├── signals.py
│   ├── views.py
│   └── rectangle.py
│
├── manage.py
├── test_rectangle.py
├── requirements.txt
└── README.md
```

# How to Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Create database migrations

```bash
python manage.py makemigrations
```

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Check the project

```bash
python manage.py check
```

### 5. Start the Django server

```bash
python manage.py runserver
```

### 6. Test the Django Signals questions

Open the following URLs in your browser:

- Question 1: `http://127.0.0.1:8000/q1/`
- Question 2: `http://127.0.0.1:8000/q2/`
- Question 3: `http://127.0.0.1:8000/q3/`

The execution details and outputs can be checked in the terminal.

### 7. Test the Rectangle class

Run the following command:

```bash
python test_rectangle.py
```

## Final Note

This assignment helped me understand Django Signals, Python threading, database transactions, and custom Python iterators through practical implementation.

I have included the code and testing files in this repository so that each solution can be reviewed and executed separately.