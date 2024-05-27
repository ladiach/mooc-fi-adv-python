# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    
    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
    
    
class MostVowels(WordGame):
    
    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word:str, player2_word:str):
        vowels ="AEIOUaeiou"
        vowels_player1 = sum(player1_word.count(vowel) for vowel in vowels)
        vowels_player2 = sum(player2_word.count(vowel) for vowel in vowels)
    
        if vowels_player1 > vowels_player2:
            return 1
        elif vowels_player2 > vowels_player1:
            return 2
            
    
class RockPaperScissors(WordGame):
    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word:str, player2_word:str):
        valid_answers = ["rock", "paper", "scissors"]
        valid_player1 = False
        valid_player2 = False
    
        if player1_word not in valid_answers and player2_word not in valid_answers:
            return False
        
        if player1_word not in valid_answers:
            return 2
    
        if player2_word not in valid_answers:
            return 1
    
        if player1_word == player2_word:
            return False
    
        if player1_word == "rock":
            if player2_word =="scissors":
                return 1
            else:
                return 2
        elif player1_word == "paper":
            if player2_word == "rock":
                return 1
            else:
                return 2
        elif player1_word =="scissors":
            if player2_word == "paper":
                return 1
            else:
                return 2
        else:
            return False #tie
    
if __name__ == "__main__":
    p = MostVowels(3)
    p.play()