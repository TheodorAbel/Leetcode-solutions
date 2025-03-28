"""
Two Sum - LeetCode Solution
Returns indices of two numbers that add up to the target.
"""

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i

# Example usage
if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
