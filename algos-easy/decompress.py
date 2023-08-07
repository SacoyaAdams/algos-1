# Decompress

# Write a function, decompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an decompressed version of the string where each 'char' of a group 
# is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.


def decompressed(s):
    result = []
    i = 0
    j = 0
    # iterate thru the loop and when i hit an alph char, it needs to switch 
    numbers = '0123456789'
    while j < len(s):
        # check if it's an interger
       if s[j] in numbers:
           j += 1
       else:
           # extract number from strin using the difference between i and j
           num = int(s[i:j])
           # multiply the number by character -> store in result list
           result.append(num * s[j])
           # increment j, catch i up to j 
           j += 1
           i = j 
    return ''.join(result)


















# def decompress(s):
#     newstring= ''
#     factor = ""
#     substring = ""
#     for char in s:
#         if char.isnumeric():
#             factor += char
#         else:
#             char.isalpha()
#             substring = (char)*int(factor)
#             newstring += substring
#             factor = ""
#         return newstring
    # i = 0
    # while i < len(s):
    #     count = int(s[i])
    #     char = s[i + 1]
    #     decompressed += count * char
    #     i += 2
    # return decompressed

"""
The decompress function is defined, which takes a string s as an argument.

An empty string decompressed is initialized to store the decompressed result.

The variable i is initialized to 0. It will be used as an index to iterate through the input string s.

The while loop begins. It continues as long as i is less than the length of the string s.

Inside the loop, the character at index i is converted to an integer using int(s[i]) and assigned to the variable count. This represents the number of times the character will be repeated.

The character at index i+1 is assigned to the variable char. This represents the character to be repeated.

The decompressed string decompressed is updated by adding count number of char using the repetition operator *. This repeats the character char count times and concatenates it to the existing decompressed string.

The variable i is incremented by 2 to move to the next pair of number and character in the string.

Once the loop ends, the fully decompressed string is stored in the decompressed variable.

Finally, the decompressed string is returned as the output of the function.

By running the test case decompress("2c3a1t"), you will get the expected output of 'ccaaat', where the 'c' is repeated twice, 'a' is repeated three times, and 't' appears once.
"""


# TEST CASE
print(decompress("2c3a1t"))  # Output: 'ccaaat'




# TEST CASES
decompress("2c3a1t") # -> 'ccaaat'
# decompress("4s2b") # -> 'ssssbb'
# decompress("2p1o5p") # -> 'ppoppppp'
# decompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
# decompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
