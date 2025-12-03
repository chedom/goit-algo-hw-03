class Tower:
    def __init__(self, name: str, capacity: int):
        self.stack = []
        self.capacity = capacity
        self.name = name

    def add_disk(self, disk: int):
        if self.is_empty() or self.stack[-1] > disk:
            self.stack.append(disk)
            return True

        return False

    def pop_disk(self) -> int | None:
        if self.is_empty():
            return None

        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def peek_disk(self) -> int | None:
        if not self.is_empty():
            return self.stack[-1]

    def has_largest_disk(self) -> bool:
        if self.is_empty():
            return False

        return self.stack[0] == self.capacity

    def size(self) -> int:
        return len(self.stack)

    def is_full(self) -> bool:
        return self.size() == self.capacity

    def is_allowed(self, disk: int) -> bool:

        if self.is_empty():
            return True

        return self.stack[-1] > disk

    def __str__(self) -> str:
        return f"'{self.name}': {self.stack}"
