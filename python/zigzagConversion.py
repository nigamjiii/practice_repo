class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res_arr = ['']*numRows
        i = 0
        br = False

        while i < len(s) and br != True:

            for j in range(numRows):
                if i < len(s):
                    res_arr[j] += s[i]
                    i += 1
                else: 
                    br = True
                    break

            for k in range(numRows - 2, 0, -1):
                if i < len(s):
                    res_arr[k] += s[i]
                    i += 1
                else: 
                    br = True
                    break

        res = ''   
        for i in range(numRows):
            res += res_arr[i]

        return res
    
link = 'https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150'