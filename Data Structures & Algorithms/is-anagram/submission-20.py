class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        count_hashmap = defaultdict(int);

        for char in s:
            count_hashmap[char] += 1
        for char in t:
            count_hashmap[char] -= 1
            if count_hashmap[char] < 0:
                return False
        
        return True