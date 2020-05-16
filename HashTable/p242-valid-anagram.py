class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = dict()
        for a in s:
            if a in map:
                map[a] += 1
            else:
                map[a] = 1
        for b in t:
            if b in map and map[b] > 0:
                map[b] -= 1
            else:
                return False
        for k, v in map.items():
            if v > 0:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    r1 = s.isAnagram("anagram", "nagaram")
    r2 = s.isAnagram("rat", "car")
    r3 = s.isAnagram("rat", "r")
    print(r1, r2, r3)