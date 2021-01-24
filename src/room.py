# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, loot=[]):
        self.name = name
        self.description = description
        self.loot = loot

    def __str__(self):
        return f"\nCurrent Location: {self.name} : {self.description}\n available loot: {self.loot}"

    # def print_loot(self):
    #     p = [f"{i.name} {i.description}" for i in {self.loot}]
    #     print(p)
