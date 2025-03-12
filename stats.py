def word_count(text):
        return len(text.split())

def character_count(text):
	lower = text.lower()
	c_count = {}
	for character in lower:
		if character in c_count:
			c_count[character] += 1
		else:
			c_count[character] = 1
	return c_count

def sorted_count(char_dict):
	chars_list = []
	for char,count in char_dict.items():
		chars_list.append({"char": char, "count": count})
	def sort_on(dict_item):
		return dict_item["count"]
	chars_list.sort(reverse=True, key=sort_on)
	return chars_list
