import difflib

def approximate_search(word, strings, k):
    matches = difflib.get_close_matches(word, strings, k)
    return matches

# Read the text file and store it in-memory
with open('file.txt', 'r') as f:
    strings = f.read().splitlines()

# Wait for user input and return a list of suitable suggestions
word = input('Enter a word: ')
matches = approximate_search(word, strings, 1)
print(matches)