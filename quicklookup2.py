#!/usr/local/bin/python3

import sys


def get_lines(filename=""):

	if not filename:
		print("File name not specified.")
		filename = [input("Please enter name of data file: ")]

	try:
		file = open(filename[0], "r", encoding="utf8")
	except IOError:
		print("File does not exist.")
		return "Nothing to print."

	lines = file.readlines()
	file.close()

	return lines


# Function to read in the file contents if the file exists
def read_file(filename=""):

    # File exist error handling - http://www.diveintopython.net/file_handling/index.html
    try:
        current_file = open(filename, "r", encoding="utf8")
    except IOError:
        print("File does not exist.")
        return "Nothing to print."

def clean_words(dataline):

	listofwords = dataline.split()
	for word in listofwords:
		word = word.lower()
		word = word.strip(".,!?'\"")
		yield word


def get_dictionary(lines):
	words = {}
	linenum = 1
	
	for line in lines:
		for word in clean_words(line):
			if word in words:
				words[word].add(linenum)
			else :
				words[word] = {linenum}
	
		linenum += 1

	return words


def get_commonlines(words, input_words):
	listofwords = input_words.split()

	if len(listofwords) == 0:
		answerset = set()
	else:
		answerset = words.get(listofwords[0].lower(), set())

		for word in listofwords[1:]:
			answerset = answerset & words.get(word.lower(), set())

	return answerset


def print_commonlines (datalines, commonlines, query_words):

	for line in commonlines :
		outline = datalines[line - 1]
		lowerline = outline.lower()
		
		for word in query_words:
			index = 0 
			while index != -1:
				index = lowerline[index:].find(word.lower())
				if index != -1:
					outline = outline[0:index] + word.upper() + outline[index + len(word):]
					index += len(word)

		print(line, ":", outline)


lines = get_lines(sys.argv[1:])
word_dict = get_dictionary(lines)

again = 'y'

while again == 'y':
	query = input("Please enter a group of words to search for: ")

	commonlines = get_commonlines(word_dict, query)

	print_commonlines(lines, sorted(list(commonlines)), query.split())

	again = input("Do you want to do it again? ")
