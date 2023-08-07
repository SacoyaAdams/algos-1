# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
    # anagram is a word or phrase made by rearranging the letters of another word or phrase
    # use the sort method, it rearranges the elements
    # compare the sorted versions, to make sure they contain the same characters
    if (sorted(s1) == sorted(s2)):
        # if they contain the same characters, print True
        print(True)
    else:
        # else print False
        print(False)








# # TEST CASES
# anagrams('restful', 'fluster') # -> True
# anagrams('cats', 'tocs') # -> False
anagrams('monkeyswrite', 'newyorktimes') # -> True
# anagrams('paper', 'reapa') # -> False
# anagrams('elbow', 'below') # -> True
# anagrams('tax', 'taxi') # -> False
# anagrams('taxi', 'tax') # -> False
# anagrams('night', 'thing') # -> True
# anagrams('po', 'popp') # -> False
# anagrams('pp', 'oo') # -> False
