from collections import Counter

def diffBetweenTwoStrings(source, target):
  source_dict = Counter(source)
  target_dict = Counter(target)
  result = []
  
  for char in target:
    if(char in source_dict):
      if(source_dict[char]  == target_dict[char]):
        result.append(char)
      elif(source_dict[char]  < target_dict[char]):
        result.append(char)
        tmp = '+' + char
        for j in range(target_dict[char] - source_dict[char]):
            result.append(tmp)
      else:
        tmp = '-' + char
        for j in range(source_dict[char] - target_dict[char]):
         result.append(tmp)
    else:
      tmp = '+' + char
      result.append(tmp)
        
  return result
        
  
solution = diffBetweenTwoStrings("ABCDEFG", "ABDFFGH")
print(solution)

["A","B","-C","D","-E","F","+F","G","+H"]


# def meeting_planner(slotA, slotB, dur):
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
#   '''
  
#   start = 0 if slotA[0][0] < slotB[0][0] else 1
#   stack = []
#   totalSum = len(slotA) + len(slotB)

#   while(len(stack) < totalSum):
#     print(stack)
#     if(start == 0):
#       stack.append(slotA.pop(0))
#       start = 1
#     else:
#       stack.append(slotB.pop(0))
#       start = 0

#     if(len(stack) > 1):
#       tmp = stack[-2][1] - stack[-1][0]
#       if(tmp >= dur):
#         return [stack[-1][0] , (stack[-1][0] + dur)]

#   return []
#   '''


# '''
# [[1,10]], [[2,3],[5,7]], 2
# '''
# slotsA = [[10, 50], [60, 120], [140, 210]]
# slotsB = [[0, 15], [60, 70]]
# dur = 8
# solution = meeting_planner(slotsA, slotsB, dur) 
  
  
  
  
  





