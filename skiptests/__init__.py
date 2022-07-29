from django.test.runner import DiscoverRunner
from django.conf import settings
import unittest

class SkipCase(unittest.TestCase):
    
    def runTest(self):
        raise unittest.SkipTest("Skipping test based on the settings")


class SkipTestRunner(DiscoverRunner):

    def build_suite(self, test_labels=None, extra_tests=None, **kwargs):

        skip_tests = settings.SKIP_TEST_CLASSES
        if len(skip_tests) > 0:
            new_suite = unittest.TestSuite()
            suite = super().build_suite(test_labels, extra_tests, **kwargs)
            for test in suite._tests:
                test_class_name = test.__class__.__name__
                if test_class_name.startswith("Test") and test_class_name in skip_tests:
                    test_name = test._testMethodName
                    setattr(test, test_name, getattr(SkipCase(), 'runTest'))
                else:
                    new_suite.addTest(test)
            return new_suite
        else:
            return super().build_suite(test_labels, extra_tests, **kwargs)