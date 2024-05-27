# WRITE YOUR SOLUTION HERE:
class SimpleDate:
	 
    def __init__(self, day:int, month:int, year:int):
        self.__day = day
        self.__month = month
        self.__year = year
    
    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"
    
    @property
    def __get_date(self):
        return self.__day + self.__month * 30 + self.__year *30*12
    
    def __eq__(self, another_date:"SimpleDate"):
        return self.__get_date == another_date.__get_date
    
    def __ne__(self, another_date:"SimpleDate"):
        return self.__get_date != another_date.__get_date
    
    def __gt__(self, another_date:"SimpleDate"):
        return self.__get_date > another_date.__get_date
    
    def __lt__(self, another_date:"SimpleDate"):
        return self.__get_date < another_date.__get_date
    
    def __add__(self, amount:int):
        tot_days = self.__get_date
        tot_days +=amount
        new_year = tot_days //30 //12
        new_month = (tot_days // 30 ) %12
        new_days = tot_days %30
        new_date = SimpleDate(new_days, new_month, new_year)
    
        return new_date
    
    def __sub__ (self, another_date:"SimpleDate"):
        self_days = self.__get_date
        another_days = another_date.__get_date
    
        return abs(self_days - another_days)
    
    
if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)
    
    d4 = d3 + 400
    print(d4)
