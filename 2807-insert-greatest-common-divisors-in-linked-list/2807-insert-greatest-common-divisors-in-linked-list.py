# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head):
        if head.next == None: 
            return head
        temp, temp2 = head, head

        while temp != None: 
            if temp.next == None: #check if can insert 
                break 
            temp2 = temp.next
            temp.next = None
            newNode = ListNode(self.gcd(temp.val, temp2.val), temp2)
            temp.next = newNode
            temp = temp2 #newNode doesn't need to be checked 
        return head
    
    def gcd(self, a, b): #gcd helper function with euclidian algorithm 
        if b == 0: 
            return a
        return gcd(b, a % b) 