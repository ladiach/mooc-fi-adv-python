# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list):
    while True:
        if len(numbers) % 5 == 0:
            break
        
        new_nr= numbers[-1]+1
        numbers.append(new_nr)
        add_numbers_to_list(numbers)