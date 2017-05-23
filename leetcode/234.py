# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def revertList(self, head):
        pre = head
        now = head.next
        pre.next = None
        while now != None:
            tmp = now.next
            now.next = pre
            pre = now
            now = tmp
        return pre
    def isPalindrome(self, head):
        if head == None:
            return True
        n = 0
        tmp = head
        while tmp != None:
            n += 1
            tmp = tmp.next
        n /= 2
        tmp = head
        for i in range(n):
            tmp = tmp.next
        tmp = self.revertList(tmp)
        t1 = head
        t2 = tmp
        flag = True
        for i in range(n-1):
            if t1.val != t2.val:
                flag = False
            t1 = t1.next
            t2 = t2.next
        if t1.val != t2.val:
            flag = False
        t1.next = self.revertList(tmp)
        return flag
    def printList(self, l):
        while l != None:
            print l.val
            l = l.next

l = ListNode("1")
l.next = ListNode("2")
l.next.next = ListNode("3")
l.next.next.next = ListNode("3")
s = Solution()
print s.isPalindrome(l)
s.printList(l)
