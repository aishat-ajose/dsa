# Base Conversion: Write a program that performs base conversion. The input is a string, an integer b1, and another
# integer b2. The string represents an integer in base br. The output should be the string representing
# the integer in base 02. Assume 2 < bt,b2 < 16. Use " N' to represent L0, "B" for 1.L,.. ., and "F" fot
# 15.

def baseConversion(int_str, base1, base2):
    str_base10 = toBase10(int_str, base1=base1)
    return toBase2(str_base10, base2)

def toBase10(int_str, base1):
    str_base10 = 0
    n = len(int_str)
    current_pow = 0

    while(current_pow < len(int_str)):
        last_digit = ord(int_str[current_pow]) - ord('0')
        str_base10 += last_digit * (base1 ** (n - 1))
        n-=1
        current_pow += 1


    return str_base10


def toBase2(str_base10, base2):
    str_base2 = []

    while(str_base10):
        hex_code = ['0',' 1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F']
        str_base2.append(hex_code[str_base10 % base2])
        str_base10 //= base2

    return ''.join(reversed(str_base2))

print(baseConversion('615', 7, 13))