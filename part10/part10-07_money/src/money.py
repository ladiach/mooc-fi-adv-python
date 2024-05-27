# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __retrieve_full(self):
        return self.__euros + (self.__cents/100)

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def __eq__(self, another:"Money"):
        return self.__retrieve_full() == another.__retrieve_full()
    
    def __ne__(self, another:"Money"):
        return self.__retrieve_full() != another.__retrieve_full()
    
    def __gt__(self, another:"Money"):
        return self.__retrieve_full() > another.__retrieve_full()
    
    def __lt__(self, another:"Money"):
        return self.__retrieve_full() < another.__retrieve_full()
    
    def __add__(self, another:"Money"):
        tot_euros = self.__euros + another.__euros
        tot_cents = self.__cents + another.__cents
    
        if tot_cents ==100:
            tot_euros +=1
            tot_cents = 0
        
        if tot_cents > 100:
            tot_euros += 1
            tot_cents -= 100
    
        return f"{tot_euros}.{tot_cents:02d} eur"
    
    def __sub__(self, another:"Money"):
        difference = self.__retrieve_full() - another.__retrieve_full()
    
        if difference >=0:
            return f"{difference:.2f} eur"
        else:
            raise ValueError(f"a negative result is not allowed")
    
    
    
if __name__ == "__main__":
    e1 = Money(4, 22)
    e2 = Money(2, 5)  # two euros and five cents
    
    print(e1-e2)
