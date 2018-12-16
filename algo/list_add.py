# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1, l2):

        if not l1:
            return l2
        if not l2:
            return l1

        L = ListNode(0)
        LL = L

        while l1 or l2:
            res = L.val
            if l1:
                res = res + l1.val
            if l2:
                res = res + l2.val

            if res < 10:
                L.val = res
                flag = False
            else:
                L.val = res - 10
                flag = True

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if not flag and not l1 and not l2:
                break

            if flag:
                L.next = ListNode(1)
            else:
                L.next = ListNode(0)
            L = L.next

        return LL

    def show(self, L):
        while L:
            print(L.val, end='\t')
            L = L.next
        print()


if '__main__' == __name__:
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(9)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(5)
    l2.next.next.next = ListNode(6)

    sl = Solution()
    L = Solution().add_two_numbers(l1, l2)

    sl.show(l1)
    sl.show(l2)
    sl.show(L)
