# Interconvert Strings and Integers: A String might encode an integer e.g., "123" encodes 123. In
# this problem, you are to irnplement methods that take a string representing an integer and retum
# the corresponding integer, and vice versa. Your code should handle negative integers. You cannot
# use library functions like int in Python

def stringToIntegerFromRight(str):
    n = len(str)
    current_index = 0
    integer_result = 0

    while n > 0:
        if (str[n-1] == '-'):
            return integer_result * -1

        current_integer = ord(str[n-1])  - ord('0')
        integer_result += current_integer * 10**current_index
        n-=1
        current_index += 1

    return integer_result

def stringToIntegerFromLeft(str):
    n = 0

    integer_result = 0

    while n < len(str):
        if (str[n] == '-'):
            pass
        else:
            current_integer = ord(str[n])  - ord('0')
            integer_result = integer_result * 10 + current_integer

        n+=1

    if(str[0] == '-'):
        return integer_result  * -1

    return integer_result


def integerToString(num):
    str_result = []
    pos_num = num if num > 0 else -1 * num

    while(pos_num > 0):
        str_result.append(chr(ord('0') + pos_num%10) )
        pos_num //= 10

    return ('-' if num < 0 else '') + ''.join(reversed(str_result))





print(integerToString(114))