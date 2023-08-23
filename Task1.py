def main():
    try:
        #Read a String statement from the command line
        user_input = input("Enter a string: ")
        if(len(user_input)==0):
            print("The input cannot be empty")
            return

        # Find out the total number of characters present in the statement
        total_characters = len(user_input)

        # Find out the total number of duplicate Characters in the statement
        char_count = {}
        for char in user_input:
            char_count[char] = char_count.get(char, 0) + 1

        total_duplicate_characters = sum(count > 1 for count in char_count.values())

        # Find out the total number of words present in the statement
        words = user_input.split()
        total_words = len(words)

        # Find out the total number of duplicate words in the statement
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        total_duplicate_words = sum(count > 1 for count in word_count.values())

        # Reverse the characters present in the statement
        reversed_characters = user_input[::-1]

        # Reverse the words present in the statement
        reversed_words = ' '.join(reversed(words))

        # Form a new statement from the reversed words
        new_statement = reversed_words

        # Remove the duplicate characters from the latest statement
        new_statement = ''.join(char for char in new_statement if char_count.get(char, 0) == 1)

        # Print the final latest String statement
        print("Original statement:", user_input)
        print("Total characters:", total_characters)
        print("Total duplicate characters:", total_duplicate_characters)
        print("Total words:", total_words)
        print("Total duplicate words:", total_duplicate_words)
        print("Reversed characters:", reversed_characters)
        print("Reversed words:", reversed_words)
        print("New statement from reversed words:", new_statement)
        print("Final statement:", new_statement)

    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()
