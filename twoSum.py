class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stack = nums
        for i in range(len(nums)):
            num1 = stack.pop()
            if (target - num1) in stack:
                return [len(stack), stack.index(target-num1) ]