
class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[j] == self.target - self.nums[i]:
                    return [i, j]


sol = Solution([1, 2, 3], 4)
print(sol.twoSum())  
sol = Solution([2, 7, 11, 15], 9)
print(sol.twoSum())
sol=Solution([3, 2, 4], 6)
print(sol.twoSum())
sol = Solution([3, 3], 6)
print(sol.twoSum())
