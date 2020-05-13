from time import sleep

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.string_description import StringDescription


class Eventually(BaseMatcher):


    def __init__(self, matcher, timeout=10):
        super(Eventually, self).__init__()

        match_fun = getattr(matcher, 'matches', None)
        if match_fun is None or not callable(match_fun):
            raise TypeError("Eventually must be called with a hamcrest matcher argument.")

        self.matcher = matcher
        self.timeout = timeout

    def matches(self, value):
        if not callable(value):
            raise TypeError("{} is not callable. Eventually is only usable with callable objects.".format(value))
        self.wait_for(value, self.matcher, self.timeout)
        return True

    def __str__(self):
        return "Eventually {}".format(self.matcher)

    def wait_for(self, refresh_fn, matcher, timeout):
        matched = False
        counter = 0
        failure_message = StringDescription()
        while not matched and counter <= timeout:
            new_value = refresh_fn()
            match = matcher.matches(new_value)
            if not match:
                sleep(1)
                counter += 1
            else:
                matched = True

        if matched:
            return
        else:
            matcher.describe_mismatch(new_value, failure_message)
            raise AssertionError("After {} seconds test failed: {}".format(timeout, failure_message))


def eventually(matcher, timeout=10):
    return Eventually(matcher, timeout=timeout)
