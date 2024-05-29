# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []
    
    def is_empty(self):
        return True if len(self.people) == 0 else False
    
    def add(self, person:Person):
        self.people.append(person)
    
    def print_contents(self):
        tot_height =0
        for person in self.people:
            tot_height += person.height
        print(f"There are {len(self.people)} persons in the room, and their combined height is {tot_height} cm")
    
        for person in self.people:
            print(f"{person.name} ({person.height} cm)")
    
    def shortest(self):
        if len(self.people) == 0:
            return None
    
        shortest_height = self.people[0].height
        shortest = self.people[0]
    
        for i,person in enumerate(self.people):
            if person.height < shortest_height:
                shortest_height = person.height
                shortest = self.people[i]
    
        return shortest
    
    def remove_shortest(self):
        if len(self.people) == 0:
            return None
    
        to_remove = self.shortest()
    
        self.people.remove(to_remove)
    
        return to_remove     
    
    
    
    
    
    
if __name__ == "__main__":
    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    room.remove_shortest()
    room.print_contents()


