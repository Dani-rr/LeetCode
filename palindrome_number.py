def isPalindrome(x):
    stringPalindrome = str(x)
    comparisonString = ""
    for i in range(len(stringPalindrome) - 1, -1, -1):
        comparisonString += stringPalindrome[i]
    return comparisonString == stringPalindrome
        

print(isPalindrome(212))
print(isPalindrome(-121))
print(isPalindrome(10))