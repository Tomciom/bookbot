def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(path_to_file):
    text = get_book_text(path_to_file)
    words = text.split()
    return len(words)

def get_char_count(path_to_file):
    text = get_book_text(path_to_file)
    text = text.lower()
    words = text.split()

    char_dict = {}
    
    for word in words:
        for ch in word:
            if ch not in char_dict:
                char_dict[f'{ch}'] = 1
            else:
                char_dict[f'{ch}'] += 1
    return char_dict

def sort_on(items):
    return items['num']

def sort_dict(char_dict):
    sorted_dict = []
    for ch in char_dict:
        if not ch.isalpha():
            continue
        sorted_dict.append(dict(char = ch, num = char_dict[f'{ch}']))
    sorted_dict.sort(reverse = True, key = sort_on)
    return sorted_dict
