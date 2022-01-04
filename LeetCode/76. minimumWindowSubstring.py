from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        ans = float('inf'), None, None
        
        if not t or not s:
            return ""
            
        hashMap = Counter(t)
        
        start, end = 0, 0
        
        required  = len(hashMap)
        formed = 0
        windowHashMap = {}
        
        while(end < len(s)):
            char = s[end]
            windowHashMap[char] = windowHashMap.get(char, 0) + 1
            
            if(char in hashMap and windowHashMap[char] == hashMap[char]):
                formed += 1
                
            while(start <= end and formed == required):
                start_char = s[start]
                
                if (end - start + 1) < ans[0]:
                    ans = (end - start + 1, start, end)
                  
                windowHashMap[start_char] -= 1
                if(start_char in hashMap and windowHashMap[start_char] < hashMap[start_char]):
                    formed -= 1
                
                start += 1
            
            end += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]

solution  = Solution()
ans = solution.minWindow(s="ADOBECODEBANC", t='ABC')
print(ans)