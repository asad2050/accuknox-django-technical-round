### Topic: Django Signals

---

### Question 1: Are Django signals executed synchronously or asynchronously?

**Answer:**  
By default, Django signals are executed synchronously. This means that the signal handlers run in the same flow as the code that sends the signal.

**Code Snippet:**

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

# Receiver function
@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal handler executed!")

# Sending the signal
instance = MyModel.objects.create(name="Test")
print("After instance creation")  # This will only print after the handler finishes
```

In this example, `"After instance creation"` will only print after `"Signal handler executed!"` is printed, proving that the signal is processed synchronously.

---

### Question 2: Do Django signals run in the same thread as the caller?

**Answer:**  
Yes, Django signals run in the same thread as the caller. This means that the signal handlers are executed in the same thread context as the code that triggers them.

**Code Snippet:**

```python
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

# Receiver function
@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print(f"Signal handler executed in thread: {threading.current_thread().name}")

# Sending the signal
instance = MyModel.objects.create(name="Test")
print(f"Signal sent from thread: {threading.current_thread().name}")
```

When this code runs, both print statements will show the same thread name, confirming they run in the same thread.

---

### Question 3: Do Django signals run in the same database transaction as the caller?

**Answer:**  
Yes, by default, Django signals run in the same database transaction as the caller. If the transaction is rolled back, the effects of the signal handlers will also be rolled back.

**Code Snippet:**

```python
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

# Receiver function
@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal handler executed!")
    raise Exception("Simulating an error to trigger rollback")

# Sending the signal within a transaction
try:
    with transaction.atomic():
        instance = MyModel.objects.create(name="Test")
        print("Instance created!")
except Exception as e:
    print(f"Transaction rolled back: {e}")

# Check if the instance was saved
if MyModel.objects.filter(name="Test").exists():
    print("Instance exists in DB")
else:
    print("Instance does not exist in DB")  # This should print
```

In this example, the exception raised in the signal handler causes the entire transaction to roll back, proving that signals are executed within the same transaction context.
