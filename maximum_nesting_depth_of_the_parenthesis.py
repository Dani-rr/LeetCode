class Solution:
    def maxDepth(self, s: str) -> int:
        max = 0
        total_max = 0
        n = len(s)

        # Traverse the input string
        for i in range(n):
            if S[i] == '(':
                max += 1

                if max > total_max:
                    total_max = max
            elif S[i] == ')':
                if max > 0:
                    max -= 1
                else:
                    return -1

        # finally check for unbalanced string
        if max != 0:
            return -1

        return total_max