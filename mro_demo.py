"""
MRO (Method Resolution Order) is the algorithm Python uses to determine which
method or attribute to use when a class inherits from multiple parent classes.
Python searches classes in a specific order called MRO .
"""


class RequestHandler:

    def process(self):
        print("Base request processing")


class LoggingMixin(RequestHandler):

    def process(self):
        print("Logging request")
        # `super()` goes to next class in MRO. Always write:
        #   `super().method()`
        # instead of:
        #   `ParentClass.method()`
        # This allows the MRO to work correctly
        super().process()


class AuthenticationMixin(RequestHandler):

    def process(self):
        print("Authenticating user")
        super().process()


class MetricsMixin(RequestHandler):

    def process(self):
        print("Recording metrics")
        super().process()


class ApiHandler(LoggingMixin, AuthenticationMixin, MetricsMixin):
    pass


def main():
    handler = ApiHandler()

    handler.process()

    print(ApiHandler.mro())


if __name__ == "__main__":
    main()
