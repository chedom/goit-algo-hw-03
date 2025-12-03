class Tower:
    def __init__(self, name: str):
        self.stack = []
        self.name = name

    def add_disk(self, disk: int):
        if len(self.stack) > 0 and self.stack[-1] < disk:
            raise ValueError(f"Disk {disk} is larger than the top disk {self.stack[-1]}")

        self.stack.append(disk)

    def pop_disk(self) -> int | None:
        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    def __str__(self) -> str:
        return f"'{self.name}': {self.stack}"
