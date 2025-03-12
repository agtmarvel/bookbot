import sys
if len(sys.argv) == 2:
	print(sys.argv)
else:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text (filepath):
	with open(filepath) as f:
		book_text = f.read()
	return book_text
from stats import word_count
from stats import character_count
from stats import sorted_count
def main():
	book_text = get_book_text(sys.argv[1])
	num_words = word_count(book_text)  # Call the function
	count_characters = character_count(book_text)
	sorted_chars = sorted_count(count_characters)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]} ...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
# Print each character and its count
	for char_dict in sorted_chars:
		char = char_dict["char"]
		count = char_dict["count"]
        # Only print alphabetical characters
		if char.isalpha():
			print(f"{char}: {count}")
	print("============= END ===============")
main()

