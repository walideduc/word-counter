import os
import sys
# Logics
def countWords(sentence):
    words = sentence.split()
    word_occurrences = dict()
    for word in words:
        word_occurrences[word] = word_occurrences.get(word,0) + 1
    return word_occurrences
# Presentation
def presentResults(word_occurrences):
    for word , occurrence in word_occurrences.items():
        print ( 'The word "{}" appears {} time(s) in the sentence.'.format(word,occurrence))

# Input/output
try:
    sentence = os.environ['SENTENCE']
    presentResults(countWords(sentence))
except:
    print("ERROR: Please, provide a sentence to the application with the --env flag as shown in the readme.")
    sys.exit(1)
