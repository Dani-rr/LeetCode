class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        not_allowed = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    not_allowed += 1
                    break
        output = len(words) - not_allowed
        return output