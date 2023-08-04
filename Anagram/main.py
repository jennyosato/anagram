# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from operator import truediv
from re import X


def find_anagram(word, anagram):
    # [assignment] Add your code here
    words = word.replace(" ", "").lower()
    anag = anagram.replace(" ", "").lower()
    if sorted(words) == sorted(anag):
        return True
    else:
        return False


find_anagram("stool", "loots")
