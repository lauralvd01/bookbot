def get_num_words(text) :
    return len(text.split())

def get_characters_count(text) :
    dir = {}
    for char in text :
        if char.lower() in dir.keys():
            dir[char.lower()] += 1
        else :
            dir[char.lower()] = 1
    return dir

def sort_characters_count(dir) :
    list = [(char,dir[char]) for char in dir.keys() if char.isalpha()]
    list.sort(key = lambda value : value[1],reverse = True)
    return list