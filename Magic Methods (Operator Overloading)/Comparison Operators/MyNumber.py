class MyNumber:
    # Constructor initializing object with given value
    def __init__(self, value):
        self.value = value


    # 1. Function that returns true if the number is less than the given number
    def __lt__(self, other):
        return self.value < other.value

    # 2. Function that returns true if the number is less than or equal to the given number
    def __le__(self, other):
        return self.value <= other.value

    # 3. Function that returns true if the number is equal to the given number
    def __eq__(self, other):
        return self.value == other.value

    # 4. Function that returns true if the number is no equal to the given number
    def __ne__(self, other):
        return self.value != other.value

    # 5. Function that returns true if the number is greater than the given number
    def __gt__(self, other):
        return self.value > other.value

    # 6. Function that returns true if the number is greater than or equal to the given number
    def __ge__(self, other):
        return self.value >= other.value