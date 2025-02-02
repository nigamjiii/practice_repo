class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = {}
        for i in range(len(magazine)):
            if magazine[i] not in hash_map:
                hash_map[magazine[i]] = 1
                continue
            hash_map[magazine[i]] += 1

        for i in range(len(ransomNote)):
            if hash_map.get(ransomNote[i]) != None and hash_map.get(ransomNote[i]) != 0:
                hash_map[ransomNote[i]] -= 1
            else:
                return False

        return True
        
link = 'https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150'