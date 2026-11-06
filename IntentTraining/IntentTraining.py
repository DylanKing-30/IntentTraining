#   IntentTraining.py   -    Dylan King     -   November 6, 2026
#
#   Description:    This program is intended to help me learn machine learning and user intention for my personal AI assistant

##___________________________________________________________
##  Imports
import string
from collections import Counter

##___________________________________________________________
##  Functions

    #   Tokenizer that breaks sentences into individual words
def tokenize(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(
        str.maketrans("", "", string.punctuation)
        )
    return sentence.split()

    #   Word counter
def count_words(training_data):
    word_counts = {}    #   creates an empty dictionary to store word frequencies

    for intent, sentences in training_data.items(): #   goes through dictionary one category at a time
        word_counts[intent] = Counter() #   creates an empty word counter for that category

        for sentence in sentences:  #   goes through each sentence, tokenizes it, and updates the counter
            words = tokenize(sentence)
            word_counts[intent].update(words)

    return word_counts  #   sends the completed dictionary back to main()

def count_total_words(word_counts): #   uses the dictionary created in count_words()
    total_words = {}    #   creates an empty dictionary

    for intent, counts in word_counts.items():  #   loops through each intent and its word frequencies
        total_words[intent] = sum(counts.values())  #   adds together all the word frequences

    return total_words
##___________________________________________________________
##  Training Data
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

##____________________________________________________________
##  Main Program

def main():
    # Count the words in the training data
    word_counts = count_words(training_data)    #   Calls function count_words()

    # Display the results for each intent
    for intent, counts in word_counts.items():  #   Loops through each intent
        print(f"\nIntent: {intent}")

        for word, count in counts.items():  #   Loops through the words and prints how often each appears
            print(f"{word}: {count}")

    print()
    print()

    #   Count the total words in an intent
    total_words = count_total_words(word_counts)

    #   Display the total words in each intent
    for intent, total in total_words.items():
        print(f"{intent}: {total}")

if __name__ == "__main__":  #   Personal preference making main() run on open
    main()