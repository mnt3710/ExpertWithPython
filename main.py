import corpus_toolkit as ct
import corpus_nlp as tg
import os
import sys
import glob

# feature 3
print("Input the directory name containing corpus file.")
dir_name = input()

if(not os.path.isdir(dir_name)):
  print(dir_name + " doesn't exist. \nInput the name of a directory that exists.")
  sys.exit()