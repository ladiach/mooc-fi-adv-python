# WRITE YOUR SOLUTION HERE:
def filter_forbidden(to_filter:str, stops:str):
    return "".join([cr for cr in to_filter if not cr in stops])