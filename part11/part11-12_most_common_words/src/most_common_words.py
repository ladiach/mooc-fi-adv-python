import string
def remove_punct(word:str):
    word_filtered = ''
    for cr in word:
        if cr not in string.punctuation:
            word_filtered += cr

    return word_filtered



def most_common_words(filename, lower_limit:int):
    with open(filename, "r") as file:
        content_filtered = []
        for line in file:
            words = line.strip().split(" ")
            for word in words:
                content_filtered.append(remove_punct(word))    
        wc= {word:content_filtered.count(word) for word in content_filtered}
    return {word:count for word, count in wc.items() if count >= lower_limit}
    return wc





if __name__ == "__main__":
    test = most_common_words("comprehensions.txt", 3)
    print(test)