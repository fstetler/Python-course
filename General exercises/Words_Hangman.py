



import random

WORDLIST = 'Hangman.txt'


def get_random_word(min_word_length):

	num_words_processed = 0
	curr_word = None
	with open(WORDLIST, 'r') as f:
		for word in f:
			