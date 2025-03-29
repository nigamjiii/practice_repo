class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        tot_1 = s.count('1')
        n = len(s)

        if tot_1 == 0:
            return 0
        
        if tot_1 == n:
            return n

        t = '1' + s + '1'
        left_zero = 0
        i = 1
        ans = tot_1

        while i<= n:
            if t[i] == '0':
                left_zero += 1
            elif t[i] == '1' and left_zero > 0:
                temp = tot_1

                while t[i] == '1' and i<= n:
                    i += 1
                
                right_zero = 0
                while t[i] == '0' and i<= n:
                    right_zero += 1
                    i += 1

                if right_zero > 0:
                    temp += left_zero + right_zero

                ans = max(temp, ans)
                i -= 1
                left_zero = right_zero
            
            i += 1
        
        return ans

                

link = 'https://leetcode.com/problems/maximize-active-section-with-trade-i/'