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
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def traverse(self, n):
        if  n.next:
            return self.traverse(n.next) + str(n.val)
        else:
            return str(n.val)

    def array2ListNode(self,arr):
        if not arr:
            return None

        head = ListNode(arr[0])
        current = head

        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next

        return head

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        print('\n--- addTwoNumbers ---')
        n1 = int(ListNode().traverse(l1))
        n2 = int(ListNode().traverse(l2))
        print(n1,n2)
        sum1 = n1+n2
        result = [ int(d) for d in str(sum1)[::-1]]
        print(result)
        ln= ListNode().array2ListNode(result)
        t_ln= ListNode().traverse(ln)
        print('✅',ln, t_ln)

l1=ListNode().array2ListNode([2,4,3]); print('ListNode l1 :: ',ListNode().traverse(l1), l1)
l2=ListNode().array2ListNode([5,6,4]); print('ListNode l2 :: ',ListNode().traverse(l2), l2)
print(Solution2().addTwoNumbers(l1, l2))

## https://leetcode.com/problems/median-of-two-sorted-arrays/description/ | 4 (H)
class Solution4:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        print('\n--- findMedianSortedArrays ---')
        n1 = len(nums1)
        n2 = len(nums2)
        arr = nums1 + nums2
        arr.sort()
        n = n1+n2
        mid = n // 2
        if n % 2 == 0:
            median = (arr[mid-1]+arr[mid])/2
            print(arr,'middle-2: ' , arr[mid], arr[mid+1], 'median: ', median)
            return median
        else:
            median = arr[mid]
            print(arr,'middle/median: ',median)
            return float(median)

print(Solution4().findMedianSortedArrays([1,3], [2]))
print(Solution4().findMedianSortedArrays([1,2], [3,4]))

# =============
class Solution7:
    def reverse(self, x: int) -> int:
        print('\n--- reverse ---')
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