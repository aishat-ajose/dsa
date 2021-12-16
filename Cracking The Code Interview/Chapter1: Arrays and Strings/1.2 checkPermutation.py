# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

from collections import Counter


def checkPermutationUsingSorting(str1, str2):
    if(len(str1) != len(str2)):
        return False

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    for i in range(len(str1)):
        if(sorted_str1[i] != sorted_str2[i]):
            return False

    return True


def checkPermutationUsingCharacterCount(str1, str2):
    if(len(str1) != len(str2)):
        return False

    char_count = [0] * 128
    
    for char in str1:
        char_count[ord(char)] += 1
    
    for char in str2:
        if(char_count[ord(char)] == 0):
            return False
        char_count[ord(char)] -= 1
    
    return True


def ccheckPermutationUsingPython(str1, str2):
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)

test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
)

for test_case in test_cases:
    print(test_case[2] == ccheckPermutationUsingPython(test_case[0], test_case[1]))