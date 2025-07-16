https://leetcode.com/studyplan/top-interview-150/

```python
"""
✅ 1. nums1[:] = nums1_new + nums2
Modifies the existing nums1 list in-place

❌ 2. nums1 = nums1_new + nums2
Rebinds nums1 to a new list
"""

nums1[:] = nums1_new + nums2

# slice single item from list from index i
#In slicing, Python does not raise an IndexError if the end index is out of bounds.
my_list = ['a', 'b', 'c', 'd']
i = 3
print(my_list[i:i+1])  # Output: ['d']
```