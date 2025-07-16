class Solution189:
    def rotate(self, nums, k: int) -> None:
        # k can be more than length of nums
        k = k % len(nums)
        # [12345] k=4 | [123][45] | [45][123]
        nums[:] = nums[-k::] + nums[:-k:]
        print(nums)
print(Solution189().rotate([1,2,3,4,5], 3))

class Solution191:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]
        print(n,b)
        return str(b).count('1')

print(Solution191().hammingWeight(123))