from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in word_map:
                word_map[sorted_word] = []
            word_map[sorted_word].append(word)
    
        return list(word_map.values())
        
link = 'https://leetcode.com/problems/group-anagrams/'