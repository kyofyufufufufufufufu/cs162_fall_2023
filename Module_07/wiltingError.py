"""creating WiltError parent class and Overwatering child class."""

class WiltingError(Exception):
    def __init__(self, message):
        super().__init__(message)

class OverwateringError(WiltingError):
    def __init__(self, message):
        super().__init__(message)