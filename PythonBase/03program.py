# coding:utf-8
'''
    filename:03program.py
    Input a word, and then, find the vowels in it.
'''
word = input("please input one word:")
word = word.split()[0].lower()
vowels = ["a", "e", "i", "o", "u"]
word_vowels = [w for w in word if w in vowels]
if bool(word_vowels):
    print("the word {0} include vowels {1}".format(word, word_vowels))
else:
    print("There is no vowels in the word {0}".format(word))