class Solution:
    def addBinary(self, a: str, b: str) -> str:
        mx_len = max(len(a), len(b))
        a = a.zfill(mx_len)
        b = b.zfill(mx_len)

        res = ''
        carr = 0

        for i in range(mx_len - 1, -1, -1):
            res = str((int(a[i]) + int(b[i]) + carr)%2) + res
            carr = (int(a[i]) + int(b[i]) + carr) // 2

        if carr:
            res = '1' + res

        return res

link = 'https://leetcode.com/problems/add-binary/?envType=study-plan-v2&envId=top-interview-150'