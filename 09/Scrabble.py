def score(w):
	score = 0
	letter_value = {1:"AEIOULNRST",2:"DG",3:"BCMP",4:"FHVWY",5:"K",8:"JX",10:"QZ"}
	w = w.upper()
	for char in w:
		for valOfLetters in letter_value.items():
			for letter in letters:
				if char == letter:
					score += value
	return score

print(score('hello'))
print(score('computer'))