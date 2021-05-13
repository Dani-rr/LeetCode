def romanToInt(s: str) -> int:
    rom_int = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    lst = [x for x in s]
    lst_2 = [rom_int.get(x) for x in lst]
    checker = 1
    for i, j in zip(lst_2, lst_2[1:]):
        if i >= j:
            checker += 1
        else:
            lst_2[lst_2.index(i)] = -i
    return sum(lst_2)



romanToInt('IV')


aa = [5,100,2]
aa.index(5)