MOD = 10**9 + 7
mx_n = 10**5

fact = [1] * (mx_n)
inv_fact = [1] * (mx_n)

# Precompute factorial, inverse factorial up to n-1 using Fermat's Little Theorem  
for i in range(1, mx_n):
    fact[i] = fact[i-1] * i % MOD
    inv_fact[i] = pow(fact[i], MOD-2, MOD)

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD
        
        B = n - k  # Number of blocks
        if B < 1:
            return 0
        
        # C(n-1, k) * m * (m-1)^(B-1) mod MOD
        ans = comb(n - 1, k) * m % MOD
        ans = ans * pow(m - 1, B - 1, MOD) % MOD
        return ans
    
link = 'https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/description/?envType=daily-question&envId=2025-06-17'