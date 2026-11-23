class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            key_list = [0] * 26
            for char in string:
                key_list[ord(char) - ord('a')] += 1
            key_string = ",".join(map(str, key_list))
            hashmap[key_string].append(string)
        return list(hashmap.values())
