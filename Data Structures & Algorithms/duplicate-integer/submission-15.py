class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        the_set = set()
        for num in nums:
            if num in the_set:
                return True
            the_set.add(num)
        return False