a = "СтарыйКрым"

def split_dbl_wrds(word):
	for i in range(1, len(word)):
		if word[i].isupper():
			return word[:i] + "-" + word[i:]
	return word
 
print(split_dbl_wrds(a))