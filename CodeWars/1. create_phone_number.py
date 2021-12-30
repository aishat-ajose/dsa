# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers 
# in the form of a phone number.
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# def create_phone_number(n):
#     phone_number  = ['(']
#     phone_number.append(str(n[0]))
#     phone_number.append(str(n[1]))
#     phone_number.append(str(n[2]))
#     phone_number.append(") ")

#     phone_number.append(str(n[3]))
#     phone_number.append(str(n[4]))
#     phone_number.append(str(n[5]))
#     phone_number.append("-")
#     phone_number.append(str(n[6]))
#     phone_number.append(str(n[7]))
#     phone_number.append(str(n[8]))
#     phone_number.append(str(n[9]))

#     return "".join(phone_number)

def create_phone_number(n):
    phone_number = ['(', 'x', 'x', 'x', ')', ' ', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x']; 

    for i in range(len(phone_number)):
        if(phone_number[i] == 'x'):
            digit = str(n[0])
            phone_number[i] =  digit
            n.pop(0)

    return ''.join(phone_number)

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))
