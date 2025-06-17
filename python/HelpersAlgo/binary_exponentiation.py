def binary_expo(base, exp, mod):
    
    if exp == 0:
        return 1
    
    ans = 1
    base = base % mod
    
    if exp & 1 == 0:
        t = binary_expo(base, exp // 2, mod)
        ans *= (t * t) % mod
    else:
        t = binary_expo(base, (exp - 1) // 2, mod)
        ans *= (t * t * base) % mod
    
    return ans % mod    

# Example usage:
# base = 2456
# exp = 245688
# mod = 1000000007
# result = binary_expo(base, exp, mod)
# print(result)  # Output: 1024

# Large test cases
large_tests = [
    (2, 10**6, 10**9+7),
    (123456789, 987654321, 10**9+7)
]

for i, (b, e, m) in enumerate(large_tests, 1):
    print(f"Test {i}: base={b}, exp={e}, mod={m}")
    print(f"Result: {binary_expo(b, e, m)}\n")