class Data:

    def __init__(self, key, value, count=None):
        self.simple_key = key
        self.simple_value = value
        self.simple_count = count if count else []

    def __repr__(self):
        if not self.simple_count:
            return f"{self.simple_key}, {self.simple_value}"
        else:
            return f"{self.simple_key}, {self.simple_value},{self.simple_count}"

    def __str__(self):
        return f"{self.simple_key},{self.simple_value},{self.simple_count}"
