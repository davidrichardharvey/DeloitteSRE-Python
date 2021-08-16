from math import sqrt, ceil

class SimpleCalculator:
    def add(self, int1, int2):
        return int1 + int2

    def subtract(self, int1, int2):
        return int1 - int2

    def multiply(self, int1, int2):
        return int1 * int2

    def divide(self, int1, int2):
        return int1 / int2

class SciCalculator(SimpleCalculator):
    def find_sqrt(self, n):
        return sqrt(n) if n else None

    def find_ceil(self, n):
        return ceil(n) if n else None

