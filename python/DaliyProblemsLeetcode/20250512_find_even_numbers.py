from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        freq = [0] * 10

        for digit in digits:
            freq[digit] += 1

        for i in range(1, 10):
            if freq[i] == 0:
                continue

            freq[i] -= 1

            for j in range(0, 10):
                if freq[j] == 0:
                    continue

                freq[j] -= 1

                for k in range(0, 9, 2):
                    if freq[k] == 0:
                        continue

                    freq[k] -= 1

                    ans.append((i * 100 + j * 10 + k))

                    freq[k] += 1 # Have counted the all possibility with this k , so increase it's count

                freq[j] += 1  # Have counted the all possibility with this j , so increase it's count

            freq[i] += 1  # Have counted the all possibility with this i , so increase it's count

        return ans

link = 'https://leetcode.com/problems/finding-3-digit-even-numbers/?envType=daily-question&envId=2025-05-12'