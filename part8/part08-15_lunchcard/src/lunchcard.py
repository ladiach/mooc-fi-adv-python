# Write your solution here:
class LunchCard():
    
    def __init__(self, balance:float):
        self.balance = balance
    
    
    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_lunch(self):
        price_reg = 2.60
        if self.balance >=price_reg:
            self.balance -= price_reg
    
    def eat_special(self):
        price_spec = 4.60
        if self.balance >=price_spec:
            self.balance -= price_spec
    
    def deposit_money(self, amount:float):
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += amount
    

peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
pb = peters_card
gb = graces_card
print("Peter:", pb)
print("Grace:", gb)
peters_card.deposit_money(20)
graces_card.eat_special()
pb=peters_card
gb=graces_card
print("Peter:", pb)
print("Grace:", gb)
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
pb=peters_card
gb = graces_card
print("Peter:", pb)
print("Grace:", gb)