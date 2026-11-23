class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = defaultdict(int)
        t_hashmap = defaultdict(int)

        for char in s:
            s_hashmap[char] += 1
        for char in t:
            t_hashmap[char] += 1

        return s_hashmap == t_hashmap