

def max_ind(numbers):
    index = 0
    max = numbers[0]
    size = len(numbers)

    while index < size:
        if numbers[index] > max:
            max = numbers[index]
        index += 1
    else:
        return ('Макисмальное число найдено и равно ' + str(max))
            
            

numberrr = [-1, 8, 3, 20, -258]


print(max_ind(numberrr))