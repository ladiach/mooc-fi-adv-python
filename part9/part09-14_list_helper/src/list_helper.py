# WRITE YOUR SOLUTION HERE:
class ListHelper:
    
    @classmethod
    def greatest_frequency(cls, my_list:list):
    
        max_frequencies = 0
        max_value = ""
    
        for element in my_list:
            if my_list.count(element) > max_frequencies:
                max_frequencies = my_list.count(element)
                max_value = element
        
        return max_value
    
    @classmethod
    def doubles(cls, my_list:list):
        unique_elements = set(my_list)
        count_doubles = 0
    
        for element in unique_elements:
            if my_list.count(element) >= 2:
                count_doubles +=1
    
        return count_doubles
    
    
    
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    #print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))