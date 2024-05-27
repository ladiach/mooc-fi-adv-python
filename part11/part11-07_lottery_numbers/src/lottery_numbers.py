# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    
    def __init__(self, week_no:int, numbers:list):
        self.week_no = week_no
        self.numbers = numbers
    
    def number_of_hits(self, my_numbers:list):
        return len([my_number for my_number in my_numbers if my_number in self.numbers])
    
    def hits_in_place(self, my_numbers:list):
        return [my_number if my_number in self.numbers else -1 for my_number in my_numbers]
    