class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        wordList  = set(wordList)
        queue = []
        queue.append(beginWord)
        result = 1
        
        while(queue):
            size = len(queue)
            
            for _ in range(size):
                curr = queue.pop(0)
                curr_list = list(curr)
                
                for i in range(len(curr_list)):
                    originalChar = curr_list[i]
                    for j in range(97, 123):
                        newChar = chr(j)
                        if(originalChar == newChar): pass
                        curr_list[i] = newChar
                        newWord = "".join(curr_list)

                        if(newWord in wordList):
                            if(newWord == endWord):
                                return result + 1
                            queue.append(newWord)
                            wordList.remove(newWord)

                    curr_list[i] = originalChar
            result = result + 1
            
        return 0
        
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
solution = Solution()      
result = solution.ladderLength(beginWord, endWord, wordList)    
print(result) 
