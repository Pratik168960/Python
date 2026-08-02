
# FORMATTED STRINGS (F-STRINGS)

# formatted string are useful in situations where you dynammically generate 
# some text with ur variables  

first = 'John'
last = 'Smith'
# THE OLD WAY: String Concatenation
message = first + ' [' + last + '] is a coder'
print(message)

# while this approach perfectly works its not ideal because our text gets more 
# complicated it becomes harder to visulaize the output 
# this is where we use formatted string they make it easier to visualize the output 


# THE NEW WAY: Formatted Strings (f-strings)
msg = f'{first} [{last}] is a coder' # formatted string prefix your string with f 
# with these curly braces we are defining the placeholders or holes in our string 
# and when we run our program these holes will be filled with the value of variables
print(msg)


# output : 
# John [Smith] is a coder
# John [Smith] is a coder