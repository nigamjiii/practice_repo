from typing import List


def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        pos = 0
        temp = 0
        s = 0

        for i in range(len(gas)):
            temp += gas[i] - cost[i]

            if temp < 0:
                s += temp
                temp = 0
                pos = i + 1
        
        s += temp
        
        return -1 if s < 0 else pos

link = 'https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150'