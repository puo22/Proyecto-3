# runtime/memory.py

class MemoryManager:
    def __init__(self):
        self.table = {}
        self.total_memory = 0

    def sizeof(self, value):
        """Calcula memoria aproximada según el tipo."""
        if isinstance(value, (int, float, bool, str)):
            return 8
        if isinstance(value, list):
            return sum(self.sizeof(v) for v in value)
        return 8

    def alloc(self, name, value):
        size = self.sizeof(value)
        self.table[name] = value
        self.total_memory += size

        print(f"[MEM] {name} ocupa {size} bytes. Total = {self.total_memory} bytes.")
        return value

    def get(self, name):
        return self.table.get(name, None)


MEMORY = MemoryManager()
