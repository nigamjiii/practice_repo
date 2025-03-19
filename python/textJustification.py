from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line, size = [], 0
        i = 0

        while i < len(words):
            if size + len(words[i]) + len(line) > maxWidth:
                # Line complete
                extra_space = maxWidth - size
                between_spaces = extra_space // max(1,len(line) - 1)
                remaining_spaces = extra_space % max(1,len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += ' ' * between_spaces
                    if remaining_spaces:
                        line[j] += ' '
                        remaining_spaces -= 1

                ans.append(''.join(line))
                line, size = [], 0

            line.append(words[i])
            size += len(words[i])
            i += 1

        # To handle last iteration of line
        last_line = ' '.join(line)
        last_line += ' '*(maxWidth - len(last_line))
        ans.append(last_line)

        return ans


link = 'https://leetcode.com/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150'