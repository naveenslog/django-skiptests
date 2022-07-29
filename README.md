django-skiptests
===================

A Simple django library to skip some tests from a Django project.

https://github.com/naveenslog/django-skiptests

Usage
-----

Just add add to your settings.py::

```python
TEST_RUNNER="skiptests.SkipTestRunner"
SKIP_TEST_CLASSES = [
    # Name of the Test Class To Skip
    'TestLogin'
]
```
