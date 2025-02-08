class Solution:
    def isHappy(self, n: int) -> bool:
        n = sum(int(digit) ** 2 for digit in str(n))
        if n == 1:
            return True
        hash_set = set()
        while n != 1:
            if n in hash_set:
                return False
            hash_set.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return True


link = 'https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150'