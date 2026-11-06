#   IntentTraining.py   -    Dylan King     -   November 6, 2026
#
#   Description:    This program is intended to help me learn machine learning and user intention for my personal AI assistant

##  Imports
import string

##  Tokenizer that breaks sentences into individual words
def tokenize(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(
        str.maketrans("", "", string.puncuation)
        )
    return sentence.split()
training_data = {
    "remember": [
        "remember my favorite color",
        "save my favorite food",
        "remember my birthday"
        ],

    "recall": [
        "what is my favorite color",
        "tell me my birthday",
        "what is my favorite food"
        ],

    "math": [
        "add two numbers",
        "multiply these numbers",
        "calculate a number"
        ]
    }