from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    prev = 0
    prev1 = -1

    for i in range(1, n):
        curr = prev + abs(heights[i] - heights[i-1])
        if i > 1:
            curr = min(curr, prev1 + abs(heights[i] - heights[i-2]))

        prev1 = prev
        prev = curr
        

    return prev

link = 'https://www.naukri.com/code360/problems/frog-jump_3621012?leftPanelTabValue=PROBLEM'