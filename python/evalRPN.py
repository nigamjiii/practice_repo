from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = ["*", "-", "+", "/"]

        for tok in tokens:
            if tok not in operand:
                stack.append(int(tok))
            else:
                f = stack.pop()
                s = stack.pop()

                val = 0

                if tok == "+":
                    val = f + s
                elif tok == "*":
                    val = f * s
                elif tok == "/":
                    t = abs(s) // abs(f)
                    val = (-t) if (s < 0) ^ (f < 0) else t
                else:
                    val = s - f
                stack.append(val)

        return stack[0]


link = 'https://leetcode.com/problems/evaluate-reverse-polish-notation/?envType=study-plan-v2&envId=top-interview-150'