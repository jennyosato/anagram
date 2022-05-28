# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from operator import truediv
from re import X


def find_anagram(word, anagram):
    # [assignment] Add your code here
    so = word.replace(" ", "").lower()
    yo = anagram.replace(" ", "").lower()
    if sorted(so) == sorted(yo):
        return True
    else:
        return False


find_anagram("stool", "tools")
