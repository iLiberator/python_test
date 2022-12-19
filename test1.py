#Digits Multiplication

def checkio(number: int) -> int:
    change = list(str(number))
    res = [int(i) for i in change if i != '0']
    ind = 0
    solution = 1
    while ind < len(res):
        solution = solution * res[ind]
        ind = ind + 1
    return solution
    

test = 123405

print(checkio(test))

# These "asserts" are used for self-checking
#assert checkio(123405) == 120
#assert checkio(999) == 729
#assert checkio(1000) == 1
#assert checkio(1111) == 1