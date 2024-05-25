# WRITE YOUR SOLUTION HERE:
class Recording:
	 
    def __init__(self, length:int):
        if length <0:
            raise ValueError
    
        self.__length = length
    
    @property #getter
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, l:int):
        if l < 0:
            raise ValueError
    
        self.__length = l
    
    
if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)