import corpus_toolkit as ct
import corpus_nlp as tg
import os
import sys
import glob

# feature 3
print("Input the name of the directory containing the corpus file.")
""" dir_name = input() """
dir_name = "Datasets"

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
file_name="Q dataset"

ct.find_least_similar_corpus(dir_name, file_name)

ct.write_corpus(dir_name, dir_name + "_lemmas",word_lemmatized)

# feature 13
word_upos = tg.tag_corpus(dir_name)

ct.write_corpus(dir_name ,dir_name + "_tagged",word_upos)

ct.display_context(word_lemmatized)
ct.search_pos_patterns(word_upos)
pos, count = tg.count_pos_patterns(word_lemmatized, dir_name)

""" ct.pos_least(pos, count, dir_name) """