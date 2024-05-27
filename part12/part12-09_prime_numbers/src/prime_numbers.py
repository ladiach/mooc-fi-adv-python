# Write your solution here
def is_prime(nr:int):
    if nr == 2:
        return nr
    for x in range(2, nr):
        if nr%x == 0:
            return False
    return nr +1
    
    
    
def prime_numbers():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num +=1