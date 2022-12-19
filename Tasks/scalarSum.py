firstVector = [1, 8, 3, 23]
secondVector = [3, 2, 1, 100]

index = 0
scalarSum = 0

def find_scalar_sum(value1, value2):
    index = 0
    scalarSum = 0
    while index <= (len(value1) - 1):
        scalarSum = scalarSum + value1[index] * value2[index]
        index += 1
    return print(scalarSum)

find_scalar_sum(firstVector, secondVector)