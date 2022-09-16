#!/usr/bin/env python3
#C:\Users\KimiW\Documents\5letterwords.csv
#fileName = input("What word bank? (5letterwords.csv):	")
#print(fileName)
fileName = r"C:\Users\KimiW\Documents\morewords.csv"
wordBank = open(fileName)
targetLength = 5

def HasLetter(word = "", letter = ''):
	hasletter = False
	for i in range(0, len(word)-1):
		if word[i].lower() == letter:
			hasletter = True
	return hasletter
	
knownLetters = input("What letters are in what places? (_a__z)	")
contains = input("What other letters does it contain?(be)	")
notContains = input("What letters does it not have?(al)	")

def LetterPlaced(word = "", knownLetters = ""):
	if(len(word)-1 > targetLength):
		return False
	for i in range(0, len(word)-1):
		if knownLetters[i] != '_':
			if knownLetters[i] != word[i].lower():
				return False
	for i in range(0, len(contains)):
		if HasLetter(word,contains[i]) == False:
			return False
	for i in range(0, len(notContains)):
		if HasLetter(word,notContains[i]):
			return False
	return True

passedWords = []
index = 0
for line in wordBank:
	if LetterPlaced(line,knownLetters):
		passedWords.append(line)

			

for word in passedWords:
	print(word)

wordBank.close()