class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26

        for char in word:
            ind = ord(char) - ord("a")
            freq[ind] += 1

        count = float("inf")
        prefix_sum = 0
        freq.sort()

        for i in range(26):
            if freq[i] == 0:
                continue
            dele = prefix_sum
            for j in range(25, i, -1):
                if freq[j] - freq[i] <= k:
                    break

                dele += freq[j] - freq[i] - k

            count = min(dele, count)
            prefix_sum += freq[i]

        return count

link = 'https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-at-most-k/description/?envType=daily-question&envId=2025-06-21'