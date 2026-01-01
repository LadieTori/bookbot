def sort_on(item):
    return item["num"]

def get_word_count(text):
	words = text.split()
	return len(words)

def get_character_count(text):
	char_count = {}
	unique_char = []
	characters = list(text.lower())
	for index, char in enumerate(characters):
		if char not in unique_char:
			unique_char.append(char)
			current_count = 1
			current_char = char
			for j in range(index + 1, len(characters)):
				if characters[j] == current_char:
					current_count += 1
			char_count[current_char] = current_count
	return char_count

def sort_character_count(num_characters):
	sorted_count_list = []
	for key, value in num_characters.items():
   		sorted_count_list.append({
       			"char": key,
       			"num": value,
		})
	sorted_count_list.sort(reverse=True, key=sort_on)
	return sorted_count_list
