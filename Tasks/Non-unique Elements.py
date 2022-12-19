def checkio(data: list) -> list:
    
    for i in data:
        if data.count(i) <= 1:
           data.remove(i)
    return data


test = [15, 13, 1, 0, 1, 7, 7]

print(checkio(test))

# >>> a = ["a", "b", "c", "d", "e"] >>> for item in a[:]: print item if item == "b": a.remove(item) a b c d e >>> print a ['a', 'c', 'd', 'e'] 

#assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
#assert checkio([1, 2, 3, 4, 5]) == []
#assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
#assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
#assert checkio([2, 2, 3, 2, 2]) == [2, 2, 2, 2]
#assert checkio([10, 20, 30, 10]) == [10, 10]
#assert checkio([7]) == []
#assert checkio([0, 1, 2, 3, 4, 0, 1, 2, 4]) == [0, 1, 2, 4, 0, 1, 2, 4]
#assert checkio([99, 98, 99]) == [99, 99]
#assert checkio([0, 0, 0, 1, 1, 100]) == [0, 0, 0, 1, 1]
#assert checkio([0, 0, 0, -1, -1, 100]) == [0, 0, 0, -1, -1]