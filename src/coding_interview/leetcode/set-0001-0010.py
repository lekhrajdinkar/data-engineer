## 1 https://leetcode.com/problems/two-sum/description/
class Solution1:
    def twoSum(self, nums, target: int):
        print('--- twoSum ---')
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if (nums[i] + nums[j]) == target:
                    return [i,j]

print(Solution1().twoSum([2,5,5,11],10))

## 2 https://leetcode.com/problems/add-two-numbers/
## test on leetcode
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def traverse(n):
    if not n.next:
        return traverse(n.next)
    else:
        return n.data

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        print('--- addTwoNumbers ---')
        n1 = traverse(l1)
        n2 = traverse(l2)
        print(n1,n2)
        return str(n1+n2).split()


# =============

class Solution7:
    def reverse(self, x: int) -> int:
        # print('--- reverse ---', pow(2,31))
        if 0 <= x <= pow(2, 31) - 1:
            reversed = str(x)[::-1]
            if int(reversed) > pow(2, 31) - 1:
                return 0
            return int(reversed)

        elif pow(2, 31) * -1 <= x < 0:
            reversed = str(x)[1:][::-1]
            if int(reversed)*-1 < pow(2, 31) * -1:
                return 0
            return int(reversed) * -1

        else:
            return 0

print(Solution7().reverse(2345))
print(Solution7().reverse(-2345))
print(Solution7().reverse(1534236469))
print(Solution7().reverse(-2147483648))