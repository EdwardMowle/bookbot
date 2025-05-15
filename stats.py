def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}

    for char in text:
        key = char.lower()
        
        if key not in character_count:
            character_count[key] = 0
        
        character_count[key] += 1

    return character_count

def get_sorted_character_count(text):
    return sorted(get_character_count(text).items(), key=lambda x: x[1], reverse=True)
