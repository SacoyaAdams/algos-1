# Compress

# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences of 
# the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.


def compress(s):
   
    count = 1 # keeps track of the consecutive occurences of the same character
    compressed = "" # stores the cmpressed string
    for i in range(1, len(s)):

        if s[i] == s[i - 1]:
            count += 1

        else:

            compressed += str(count) + s[i - 1]

            count = 1

            compressed += str(count) + s[-1]

        return compressed
            


# TEST CASES
compress('ccaaatsss') # -> '2c3at3s'
# compress('ssssbbz') # -> '4s2bz'
# compress('ppoppppp') # -> '2po5p'
# compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'
# compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy');  # -> '127y'
