class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            result.append(f"{len(string)}#{string}")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        l = 0
        while l < len(s):
            r = l;
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            result.append(s[l:l + length])
            l += length
        return result