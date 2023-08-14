## Advance Preparation
Prepare a virtual environment for python
In the case of macOS
```
python3 -m venv .venv
. .venv/bin/activate
```

```
pip install spacy
python -m spacy download en_core_web_sm
```

```
python3 main.py
```

## Features included in my expert system

1. count, list and order the frequency of words
2. count, list and order the frequency of keywords
3. allow user to select reference corpus

4. display the shared words/keywords in the first 20 words/keywords of each dataset
5. identify the least similiar dataset based on the lowest number of shared top 20 words/keywords of the questionned dataset
6. suggest to rule out the least similiar dataset

7. tag the part-of-speech (POS) of each word
8. allow the user to select any word or string and display the word or string in context
9. allow the user to search for POS patterns following the target word, e.g. absolutely + JJ
10. count the number of identical POS patterns in each dataset
11. identify the least similiar dataset based on the number of identical POS patterns with questionned dataset
12. suggest ruling out the least similiar dataset

## describe the expert system code