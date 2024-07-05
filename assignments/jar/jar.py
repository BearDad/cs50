class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        cookies = "🍪" * self.size
        return f"{cookies}"

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        else:
            self._size = n + self._size

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        else:
            self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
