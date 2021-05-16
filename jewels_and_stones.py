class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        output = 0
        for i in jewels:
            output += stones.count(i)
        return output

jewels = 'aA'
check = jewels.split()
print(check)