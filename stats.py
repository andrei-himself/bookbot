def count_words(string):
    words = string.split()
    return len(words)

def count_chars(string):
    chars = {}
    for char in string:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else: chars[char] = 1
    return chars

def sort_dictionaries(dict):
    def sort_on(items):
        return items["num"]
    
    dict_list = []
    for key in dict:
        dict_list.append({"name": f"{key}", "num": dict[key]})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list