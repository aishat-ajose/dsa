# Compute THE SPREADSHEET COLUMN ENCODING: Implement a function that converts a spreadsheet column id to the corresponding integeq,
#  with" N' corresponding to 1. For example, you should retum 4 for "D" ,27 for " AN' ,702 for "ZZ" , elc. How
# would you test your code?

def spreadSheetEncodeColumn(col_str):
    n = len(col_str)
    result = 0
    current_index = 0

    while(n):
        digit = ord(col_str[current_index]) - ord('A') + 1
        result += digit * (26 ** (n-1))
        n -= 1
        current_index += 1

    return result

print(spreadSheetEncodeColumn('AB'))
