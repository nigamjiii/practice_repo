import sys
import math
from collections import defaultdict, deque
from itertools import permutations, combinations
from functools import lru_cache

# Fast Input/Output
input = sys.stdin.read
def print_out(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)

# Constants
MOD = 10**9 + 7
INF = float('inf')
EPS = 1e-9

# Macros (Functions as Alternatives)
def pb(lst, val): lst.append(val)  # Push Back
def all(v): return v  # Returns the list as is (Python handles iterables natively)
def sz(x): return len(x)  # Size
f = lambda p: p[0]  # First element
s = lambda p: p[1]  # Second element

# Common Data Structures
pii = tuple[int, int]
pll = tuple[int, int]
vi = list[int]
vl = list[int]
vvi = list[list[int]]
vvl = list[list[int]]
mii = dict[int, int]
mll = dict[int, int]

# Utility Functions (Using `math` Library)
def gcd(a, b):
    """Greatest Common Divisor (using math library)."""
    return math.gcd(a, b)

def lcm(a, b):
    """Least Common Multiple."""
    return (a // math.gcd(a, b)) * b

def mod_pow(base, exp, mod=MOD):
    """Power function with modular arithmetic."""
    return pow(base, exp, mod)  # Efficient built-in function

def isqrt(n):
    """Integer square root (fast, avoids floating-point issues)."""
    return math.isqrt(n)

def factorial(n):
    """Factorial (using math library)."""
    return math.factorial(n)

# Solve Function
def solve():
    # Write your solution here
    # Example:
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print_out(sum(arr) % MOD)

# Main Function
def main():
    fastio = lambda: sys.setrecursionlimit(10**6)  # Set high recursion limit
    fastio()
    
    t = 1  # Default: 1 test case
    # Uncomment the line below if multiple test cases exist
    # t = int(input().strip())
    
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
