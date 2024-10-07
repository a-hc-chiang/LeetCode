class Solution:
    def minLength(self, s: str) -> int:
        queue = [] # queue implementation with a list
        for c in s: 
            if not queue: # add first item into queue 
                queue.append(c)
            else: 
                #cases to remove substring 
                if queue[len(queue)-1] == 'A' and c == 'B': 
                    del queue[-1]
                elif queue[len(queue)-1] == 'C' and c == 'D':
                    del queue[-1]
                else: # append because characters don't meet any criteria to remove 
                    queue.append(c)
        return len(queue)