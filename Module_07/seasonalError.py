"""creating SeasonalError exception class"""

class SeasonalError(Exception):
    def __init__(self, message):
        super().__init__(self, message)

