class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        curr_freq = [0] * 26
        Mod = 10**9 + 7

        for char in s:
            curr_freq[ord(char) - 97] += 1

        for i in range(t):
            temp_freq = [0] * 26

            for j in range(26):
                if curr_freq[j] == 0:
                    continue

                if j != 25:
                    temp_freq[j + 1] = (temp_freq[j + 1] + curr_freq[j]) % Mod
                else:
                    temp_freq[0] = (temp_freq[0] + curr_freq[j]) % Mod
                    temp_freq[1] = (temp_freq[1] + curr_freq[j]) % Mod

            curr_freq[:] = temp_freq

        return sum(curr_freq) % Mod
    
link = 'https://leetcode.com/problems/total-characters-in-string-after-transformations-i/?envType=daily-question&envId=2025-05-13'