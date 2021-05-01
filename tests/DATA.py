from dataclasses import dataclass


@dataclass
class Data:
    simple_key: str
    simple_value: int
    simple_count: int

    def __init__(self, key, value, count=None):
        self.simple_key = key
        self.simple_value = value
        self.simple_count = count if count else []

    def __repr__(self):
        return f"{self.simple_key}, {self.simple_value}"

    def __str__(self):
        return f"{self.simple_key},{self.simple_value},{self.simple_count}"
