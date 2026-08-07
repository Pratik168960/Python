
# REUSABLE FUNCTIONS & SEPARATION OF CONCERNS

# A function should generally not worry about receiving input (input()) 
# or displaying output (print()) It should do one specific job and return the result
# This way, the function can be reused anywhere (e.g., in a GUI, 
# a web app, or a terminal).
# # so these lines should not be added to the function 


def emoji_converter(message):
    words = message.split(' ')

    emojis = {
        ":)": "😀",
        ":(": "😞"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
# Right after the for loop finishes building the string, we return it!
    return output




# We handle the input and output OUTSIDE of the logic function.
message = input(">") 
print(emoji_converter(message))


'''
Example Output:
> I am so happy :)
I am so happy 😀 
'''