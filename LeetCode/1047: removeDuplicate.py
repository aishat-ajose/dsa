# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

def removeDuplicates(self, s: str) -> str:
    stack = []
    
    for char in s:
        if(stack and stack[-1][0] == char):
            stack[-1][1] += 1
            if(stack[-1][1] == 2):
                stack.pop()
        else:
            stack.append([char, 1])
            
    result = []
    for lst in stack:
        result.append(lst[0] * lst[1])
        
    return "".join(result)