from typing import List
class Solution:
    ## ✅ 1207 https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        print('--- uniqueOccurrences ---', arr)
        r = {}
        set1 = set(arr)
        for i in set1:
            count = arr.count(i)
            print(i, r)
            if count in r.keys():
                print(count, 'found again ...')
                return False
            else:
                r[count] = i

        return True

    ## ✅ 2215 https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/1704172351/?envType=study-plan-v2&envId=leetcode-75
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        print("\n---- findDifference ---")
        answer = [ set(), set() ]
        print(answer)

        for i in nums1:
            if i not in nums2:
                answer[0].add(i)
        print(answer)

        for i in nums2:
            if i not in nums1:
                answer[1].add(i)
        print(answer)

        return [ list(a) for a in answer]

    # 1657. Determine if Two Strings Are Close
    # https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

# ===========
print('1207', Solution().uniqueOccurrences([1,2,2,1,1,3]))
print('1207', Solution().uniqueOccurrences([1, 2]))
print('1207', Solution().uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))

print('✔️2215', Solution().findDifference([1, 2, 3], [2, 4, 6]))
print('✔️2215', Solution().findDifference([1, 2, 3, 3], [1, 1, 2, 2]))