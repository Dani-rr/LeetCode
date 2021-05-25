class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output=""
        for i, j in itertools.zip_longest(word1, word2, fillvalue=""):
          output=output+i+j
        return output