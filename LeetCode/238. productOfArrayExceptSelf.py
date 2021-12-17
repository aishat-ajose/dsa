# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the 
# elements of nums except nums[i].The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def product(arr):
    left = [1] * len(arr)
    right = [1] * len(arr)
    n = len(arr)

    for i in range(1, n):
        left[i] = left[i-1] * arr[i-1]

    for j in range(n-1, 0, -1):
        right[j-1] = right[j] * arr[j]

    result = []
    for x, y in zip(left, right):
        result.append(x * y)

    return result

print(product(arr=[1,2,3,4]))