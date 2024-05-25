# Write your solution here
def average(person:dict):
    p_sum = person["result1"] + person["result2"] + person["result3"]
    return p_sum/3

def smallest_average(person1:dict, person2:dict, person3:dict):
    smallest = person1

    if average(person2) < average(smallest):
        smallest = person2
    if average(person3) < average(smallest):
        smallest = person3

    return smallest


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))