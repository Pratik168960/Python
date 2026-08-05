

# DICTIONARIES IN PYTHON
# Dictionaries are used to store data in Key-Value pairs.
# Keys must be unique, but values can be anything (strings, numbers, booleans, etc.).


customer = {
    "name": "Pat",
    "age": 30,
    "is_verified": True
}

# We access the value associated with the "name" key
print(f"Customer Name: {customer['name']}")

'''
Output:
Customer Name: Pat
'''




phone = input("Phone: ")

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

output = ""
for ch in phone:
    # .get() is safer than square brackets []. 
    # If the key (ch) is not found, it returns the default value "!" instead of crashing.
    output += digits_mapping.get(ch, "!") + " "
    
print(output)

'''
Example Output:
Phone: 124
One Two Four 
'''


# EMOJI CONVERTER
# This program scans a message for text emojis and replaces them with real emojis.

message = input("> ")

# .split(' ') takes our string and breaks it into a List of words wherever there is a space.
words = message.split(' ')

emojis = {
    ":)": "😀",
    ":(": "😞"
}

output = ""
for word in words:
    # If the word matches a key in our dictionary, it returns the emoji.
    # If not, it just returns the original word.
    output += emojis.get(word, word) + " "
    
print(output)

'''
Example Output:
> Good morning :)
Good morning 😀 
'''