# WRITE YOUR SOLUTION HERE:
def recursive_sum(number:int):
    if number <=1:
        return number
    
    sum_nr =0
    sum_nr += number
    sum_nr += recursive_sum(number-1)
    return sum_nr