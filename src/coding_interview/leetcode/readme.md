https://leetcode.com/studyplan/top-interview-150/

```python

✅ nums1[:] = nums1_new + nums2
#Modifies the existing nums1 list in-place

❌ nums1 = nums1_new + nums2
#Rebinds nums1 to a new list


nums1[:] = nums1_new + nums2

# slice single item from list from index i
#In slicing, Python does not raise an IndexError if the end index is out of bounds.
my_list = ['a', 'b', 'c', 'd']
i = 3
print(my_list[i:i+1])  # Output: ['d']

list(str) ❌ => TypeError: 'type' object is not iterable
str.strip().split() ✔️ # do this

c.isalnum()
filtered = "".join(c for c in s if c.isalnum())
```