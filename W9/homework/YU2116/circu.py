class CircularQueue:
    def __init__(self, k: int):
        self.capacity = k + 1
        self.data = [0] * self.capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.capacity
        return True

    def front(self) -> int:
        if self.is_empty():
            return -1
        return self.data[self.head]

    def rear(self) -> int:
        if self.is_empty():
            return -1
        return self.data[(self.tail - 1 + self.capacity) % self.capacity]

    def is_empty(self) -> bool:
        return self.head == self.tail

    def is_full(self) -> bool:
        return (self.tail + 1) % self.capacity == self.head