# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        if len(self.numbers)>0:
            return sum(self.numbers)/len(self.numbers)
        
    def sum_even(self):
        even = [nr for nr in self.numbers if nr%2 == 0]
        return sum(even)
    
    def sum_odds(self):
        odds = [nr for nr in self.numbers if nr%2!=0]
        return sum(odds)



stats = NumberStats()
print("Please type in integer numbers:")
while True:
    n = int(input())
    if n == -1:
        break
    stats.add_number(n)

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {stats.sum_even()}")
print(f"Sum of odd numbers: {stats.sum_odds()}")