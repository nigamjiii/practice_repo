class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        len_ans = len(word) - numFriends + 1

        if len_ans == len(word):
            return word

        largest_char = max(word)
        indices = [i for i, char in enumerate(word) if char == largest_char]

        substrings = [
            word[i : i + len_ans] if i + len_ans <= len(word) else word[i:]
            for i in indices
        ]

        return max(substrings)

link = 'https://leetcode.com/problems/find-the-largest-lexicographical-string-in-a-box/?envType=daily-question&envId=2025-06-04'