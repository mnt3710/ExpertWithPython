import corpus_toolkit as ct
import corpus_nlp as tg
import os
import sys
import glob

# feature 3
print("Input the name of the directory containing the corpus file.")
""" dir_name = input() """
dir_name = "COCA_sample_text"

if(not os.path.isdir(dir_name)):
  print(dir_name + " doesn't exist. \nInput the name of a directory that exists.")
  sys.exit()


## lines 15 through is copy from https://github.com/kristopherkyle/Corpus-Methods-Intro/blob/master/Python_Tutorial_8.md
word = ct.load_corpus(dir_name)

word_tokenized = ct.tokenize(word)

word_lemmatized = ct.lemmatize(word_tokenized)

# feature 1, feature 2
lemma_greq = ct.corpus_frequency(word_lemmatized)

ct.high_val(lemma_greq)

print("Input the question corpus file name.")
""" file_name = input() """
question_corpus_name="w_acad_1990"

ct.find_least_similar_corpus(dir_name, question_corpus_name)

