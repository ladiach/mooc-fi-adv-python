# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    if employee is None:
        return 0
        
    count = 0
    
    for emp in employee.subordinates:
        count +=1
        count += count_subordinates(emp)
    
    return count