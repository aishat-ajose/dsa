# URLify: Write a method to replace all spaces in a string with'%20'You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string, (Note: if implementing in Java, please use a character array so that you can
# perform this operation in place.)

def urlify(url_str, length):
    url_list = list(url_str[:length])

    for i in range(length):
        if(url_list[i] == ' '):
            url_list[i] = '%20'

    return "".join(url_list)


def urlifyPython(url_str, length):
    return url_str[:length].replace(' ', '%20')


test_cases = [
        ("much ado about nothing      ", 22, "much%20ado%20about%20nothing") ,
        ("Mr John Smith       ", 13, "Mr%20John%20Smith"),
        (" a b    ", 4, "%20a%20b"),
        (" a b       ", 5, "%20a%20b%20"),
]

for test_case in test_cases:
    print(urlify(test_case[0], test_case[1]) == test_case[2])