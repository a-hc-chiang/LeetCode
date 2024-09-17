class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        str1List = s1.split(' ') #makes strings easy to iterate through 
        str2List = s2.split(' ') 
        map = {} # map that keeps track of the frequency of both words 

        for s in str1List: 
            if s in map.keys():
                map[s] += 1
            else: 
                map[s] = 1

        for s in str2List: 
            if s in map.keys():
                map[s] += 1
            else: 
                map[s] = 1

        for key, value in map.items(): #getting words that only appeared once between both words 
            if value == 1: 
                res.append(key)
        return res