# Write your solution here
import re
def is_dotw(my_string: str):
    abb = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    
    if re.search(abb, my_string):
        return True
    else:
        return False
    
def all_vowels(my_string:str):
    vowels = "[aeiouAEIOU]"
    
    for cr in my_string:
        if re.search(vowels, cr):
            continue
        else:
            return False
    return True
    
def time_of_day(my_string:str):
    format_time = re.compile("^(([01]\d|2[0-3]):([0-5]\d):([0-5]\d))$")
    
    return bool (format_time.match(my_string))