class Solution:
    num_sum_map = {}

    def sumDigit(self, n):
        s = 0

        while n > 0:
            s += n % 10
            n = n // 10

        return s

    def countLargestGroup(self, n: int) -> int:
        sum_map = {}
        maxi = float("-inf")
        for val in range(1, n + 1):
            dig_sum = 0
            if val not in Solution.num_sum_map:
                dig_sum = self.sumDigit(val)
                Solution.num_sum_map[val] = dig_sum
            else:
                dig_sum = Solution.num_sum_map[val]

            if dig_sum in sum_map:
                sum_map[dig_sum] += 1
            else:
                sum_map[dig_sum] = 1

            maxi = max(maxi, sum_map[dig_sum])

        c = 0

        for key, val in sum_map.items():
            if val == maxi:
                c += 1

        return c


link = 'https://leetcode.com/problems/count-largest-group/?envType=daily-question&envId=2025-04-23'