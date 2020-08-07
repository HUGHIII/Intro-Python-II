# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = []
    
    def __str__(self):
        return f"player location: {self.location}"

    def add_to_inv(self,loot):
        self.inventory.append(loot)
        self.print_inv()

    def print_inv(self):
        print("inventory : ", [f"{i.name} - {i.description}" for i in self.inventory], "\n")
