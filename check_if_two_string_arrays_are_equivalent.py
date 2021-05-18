class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string_1 = ''
        string_2 = ''
        for i in word1:
            string_1 += i
        for i in word2:
            string_2 += i
        if string_1 == string_2:
            return True
        else:
            return False
