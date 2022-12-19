#Sum Numbers


def sum_numbers(text: str) -> int:
    text = text.split()
    index = 0
    sum_digits = 0
    while index <= (len(text) - 1):
        if text[index].isdigit() == True:
            sum_digits = sum_digits + int(text[index])
        else:
            sum_digits = sum_digits
        index = index + 1
    return sum_digits

text = "This picture is an oil on canvas painting by Danish artist Anna Petersen between and 19 year"

print(sum_numbers(text))

#assert sum_numbers("hi") == 0
#assert sum_numbers("who is 1st here") == 0
#assert sum_numbers("my numbers is 2") == 2
#assert sum_numbers("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year") == 3755