class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        output = [1] * size
        for i in range(1, size):
            output[i] *= output[i - 1] * nums[i - 1]
        suffix = 1
        for i in reversed(range(size)):
            output[i] *= suffix
            suffix *= nums[i]
        return output