# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def isUniqueCharsUsingSet(str):
    if(len(str) > 128):
        return False

    char_set = [False] * 128

    for char in str:
        val_in_char_set = ord(char)
        if char_set[val_in_char_set]:
            return False
        else: 
            char_set[val_in_char_set] = True
        
    return True


def isUniqueCharsPython(str):
    return len(set(str)) == len(str)


def isUniqueCharsUsingSorting(str):
    sorted_str = sorted(str)
    for i in range(1, len(str)):
        if sorted_str[i-1] == sorted_str[i]:
            return False

    return True



test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
]

for test_case in test_cases:
    print(test_case[1] == isUniqueCharsPython(test_case[0]))