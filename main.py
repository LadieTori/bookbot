import sys
from stats import get_word_count, get_character_count, sort_character_count

def get_book_text(path):
	with open(path) as f:
		return f.read()

def main():

	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1]
	text = get_book_text(book_path) #Book Text
	num_words = get_word_count(text) #Word Count
	num_characters = get_character_count(text) #Character Count
	sorted_characters = sort_character_count(num_characters)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in sorted_characters:
		char = item["char"]
		num = item["num"]
		if not char.isalpha():
			continue
		print(f"{char}: {num}")
	print("============= END ===============")
	print(sys.argv)
main()
