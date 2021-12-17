# Palindrome Permutation: Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards, A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
from collections import Counter


def isPalindromePermutationMap(pal_str):
    hash = Counter(pal_str.replace(' ', "").lower())
    foundOdd = False

    for char in hash:
        if(hash[char]%2 == 1):
            if(foundOdd):
                return False
            foundOdd = True
    return True


test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]

for test_case in test_cases:
    print(isPalindromePermutationMap(test_case[0]) == test_case[1])