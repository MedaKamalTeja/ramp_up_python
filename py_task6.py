# Read a String statement from CMD
user_inp = input("Enter a string:")

#Total number of characters present in the statement
total_characters = len(user_inp)
print("Total number of characters:", total_characters)

#Total number of duplicate Characters in the statement
char_count = {}
for char in user_inp:
    char_count[char] = char_count.get(char, 0) + 1

total_dupe_chars = sum(count > 1 for count in char_count.values())
print("Total number of dupe characters:", total_dupe_chars)

# Total number of words present in the statement
words = user_inp.split()
total_words = len(words)
print("Total number of words:", total_words)

#Total number of duplicate words in the statement
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

total_duplicate_words = sum(count > 1 for count in word_count.values())
print("Total number of duplicate words:", total_duplicate_words)

# Reverse the characters
reverse = user_inp[::-1]
print("Reversed characters:", reverse)

# Reverse the words
reversed_words = ' '.join(reversed(words))
print("Reversed words:", reversed_words)

# Form a new statement with reversed words
new_statement = reversed_words

# Remove the duplicate characters from the latest statement
new_statement = ''.join(char for char in new_statement if char_count[char] == 1)

# Print the final String statement
print("Final statement:", new_statement)
