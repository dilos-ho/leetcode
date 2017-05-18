# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0
        numsum = 0
        i = 1
        while (l1 != None):
            num1 += l1.val * i
            i *= 10
            l1 = l1.next
        i = 1
        while (l2 != None):
            num2 += l2.val * i
            i *= 10
            l2 = l2.next
        numsum = num1 + num2
        numsum = str(numsum)
        node = None
        node2 = None
        for x in range(len(numsum)):
            node = ListNode(int(numsum[x]))
            node.next = node2
            node2 = node
        return node    
            
            
            
            
            
            
            
            
            
            
