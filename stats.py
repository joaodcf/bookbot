def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    lowercase_string = str.lower(text)
    characters = list (lowercase_string)
    character_dict = {}
    for character in characters:
        if character not in character_dict:
            character_dict[character] =1
        else:
            character_dict[character] +=1    
    return character_dict


def sorted_count(dictionary):
    sorted_dict_list = []
    for character in dictionary:
        char_dict = {"char": character, "num": dictionary[character]}
        sorted_dict_list.append(char_dict)
    
    def sort_on(dict):
        return dict["num"]

    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list