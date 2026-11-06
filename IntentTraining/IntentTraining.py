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
        "remember my favorite color is blue",
        "save my favorite food as pizza",
        "remember that my birthday is in July",
        "my favorite basketball team is the Lakers",
        "my interview is at three tomorrow",
        "I live in Ohio",
        "I really enjoy running",
        "my favorite subject is mathematics",
        "keep track of my appointments",
        "don't forget that I have practice tomorrow",
        "I want you to remember my hometown",
        "please store this information for later",
        "make a note that I have an exam Friday",
        "my dog's name is Max",
        "I prefer coffee over tea",
        "remember that I am studying engineering",
        "you should know that I like video games",
        "I usually wake up at seven",
        "save this fact about me",
        "I have a meeting scheduled for Monday"
        ],

    "recall": [
        "what is my favorite color",
        "what food do I like the most",
        "when is my birthday",
        "what is my favorite basketball team",
        "when is my interview",
        "where do I live",
        "what sport do I enjoy",
        "what subject do I like",
        "do you remember my hometown",
        "tell me what you know about me",
        "what did I tell you yesterday",
        "can you remind me of my appointments",
        "what is my dog's name",
        "do you know what I prefer",
        "what am I studying",
        "what time do I usually wake up",
        "can you recall something I told you",
        "what information have you saved about me",
        "tell me my favorite video game",
        "do you remember what I said earlier"
        ],

    "math": [
        "what is five plus three",
        "add these two numbers together",
        "calculate the sum of ten and twenty",
        "what is twelve minus seven",
        "subtract five from fifteen",
        "find the difference between twenty and eight",
        "what is six times nine",
        "multiply four by seven",
        "calculate the product of eight and three",
        "what is twenty divided by five",
        "divide one hundred by ten",
        "find the quotient of forty and eight",
        "can you solve this math problem",
        "help me calculate an equation",
        "what is the square root of sixteen",
        "what is ten squared",
        "calculate fifteen percent of two hundred",
        "how much is seven plus eleven",
        "what is the result of nine multiplied by six",
        "can you help me with a calculation"
        ],

    "forget": [
        "forget my favorite color",
        "delete my favorite food from memory",
        "forget when my birthday is",
        "remove my favorite basketball team",
        "forget the time of my interview",
        "don't remember where I live anymore",
        "erase what you know about my hobbies",
        "forget my favorite subject",
        "remove my hometown from your memory",
        "delete everything you know about me",
        "forget what I told you yesterday",
        "remove my appointments from memory",
        "forget my dog's name",
        "delete my personal preferences",
        "forget what I am studying",
        "erase my usual wake up time",
        "I don't want you to remember that anymore",
        "clear all of your saved information",
        "stop remembering my favorite video game",
        "please forget what I said earlier"
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