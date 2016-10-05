import random
from metaphone import doublemetaphone as dmphone

#Reading the file
raw_poem = open("input.txt",'r')
words = raw_poem.read().split()			#making list of words
words.append("the")
#creating the list of phonetics of words
ph_words = []
for word in words:
	try:
		phonetic = dmphone(word)[0]
		if ord(phonetic[-1]) == 48:
			phonetic = dmphone(word)[1]
		ph_words.append(phonetic)
		print word
		print ord(ph_words[-1][-1])
	except:
		pass

