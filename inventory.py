class Inventory:
    def __init__(self):
        self.slots =[]

    def add(self, item):
        self.slots.append(item)
    def __len__(self):
        return len(self.slots)

    def __contain__(self, item):
        return item in self.slots