
def isPalindrome(x):
    aa = str(x)
    lst = ''
    if x < 0:
        return False
    else:
        for i in reversed(aa):
            lst += i

    if int(lst) == x:
        return True
    else:
        return False

bb = isPalindrome(121)
print(bb)