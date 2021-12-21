# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, pie -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae - > false

def oneWay(s: str, p: str):
    s_char_map = [0] * 26
    foundEdit = False

    if(abs(len(s) - len(p)) > 1):
        return False

    for char in s:
        char_index = ord(char) - ord('a')
        s_char_map[char_index] += 1

    for char in p:
        char_index = ord(char) - ord('a')
        if (s_char_map[char_index] != 0):
            # if(foundEdit):
            #     return False
            # foundEdit = True
        
        # else:
            s_char_map[char_index] -= 1
    
    for i in range(26):
        if s_char_map[i] != 0:
            if(foundEdit):
                return False
            foundEdit = True


    return True

test_cases = [
    ['pale', 'pie' , True],
    ['pales', 'pale' , True],
    ['pale', 'bale' , True],
    ['pale', 'bae',False]
]

for test_case in test_cases:
    print(oneWay(test_case[0], test_case[1]) == test_case[2])