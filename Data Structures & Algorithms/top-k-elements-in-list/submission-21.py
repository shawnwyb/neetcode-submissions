class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in hashmap.items():
            buckets[value].append(key)
        for i in reversed(range(len(buckets))):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result