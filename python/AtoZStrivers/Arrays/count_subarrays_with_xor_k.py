from math import *
from collections import *
from sys import *
from os import *

def subarraysXor(arr, x):
    prefix_xor = {0: 1}
    curr_xor = 0
    ans = 0

    for num in arr:
        curr_xor ^= num

        if curr_xor^x in prefix_xor:
            ans += prefix_xor[curr_xor^x]

        if curr_xor in prefix_xor:
            prefix_xor[curr_xor] += 1
        else:
            prefix_xor[curr_xor] = 1

    return ans


link = 'https://www.naukri.com/code360/problems/count-subarrays-with-given-xor_1115652?leftPanelTabValue=PROBLEM'