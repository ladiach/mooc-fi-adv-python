# Write your solution here:
class Item():
    
    def __init__(self, name:str, weight:int):
        self.__name = name
        self.__weight = weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
class Suitcase():
    
    def __init__(self, max_weight:int):
        self.items = []
        self.max_weight = max_weight
        self.combined_weight = 0
    
    def __str__(self):
        if len(self.items) == 1:
            return f"1 item ({self.combined_weight} kg)"
        return f"{len(self.items)} items ({self.combined_weight} kg)"
    
    def add_item(self, item:Item):
        if self.combined_weight + int(item.weight()) < self.max_weight:
            self.items.append(item)
            self.combined_weight += item.weight()
    
    def print_items(self):
        
        for item in self.items:
            print(f"{item.name()} ({item.weight()} kg)")
    
    def weight(self):
        return self.combined_weight
    
    def heaviest_item(self):
    
        heaviest = None
        heaviest_weight = 0
    
        for item in self.items:
            if item.weight()>heaviest_weight:
                heaviest_weight = item.weight()
                heaviest = item
    
        return heaviest
    
class CargoHold():
    
    def __init__(self, max_weight:int):
        self.suitcases = []
        self.max_weight = max_weight
        self.current_weight = 0
    
    def add_suitcase(self, suitcase:Suitcase):
    
        if self.current_weight + suitcase.combined_weight <= self.max_weight:
            self.suitcases.append(suitcase)
            self.current_weight += suitcase.combined_weight
    
    def __str__(self):
        if len(self.suitcases) == 1:
            return f"1 suitcase, space for {self.max_weight - self.current_weight} kg"
    
        return f"{len(self.suitcases)} suitcases, space for {self.max_weight - self.current_weight} kg"
    
    def print_items(self):
        for suitcase in self.suitcases:
            for item in suitcase.items:
                print(f"{item.name()} ({item.weight()} kg)")
    
    
if __name__ == "name":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)
    
    suitcase = Suitcase(5)
    
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)
    
    
    print("The suitcase contains the following items:")
    suitcase.print_items()