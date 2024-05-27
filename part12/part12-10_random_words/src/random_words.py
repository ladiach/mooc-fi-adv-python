# Write your solution here:
from random import sample
def word_generator(characters: str, length: int, amount: int):
    return ("".join(sample(characters, k=length)) for i in range(amount))