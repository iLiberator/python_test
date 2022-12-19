def checkio(num: int) -> str:
    check = str(num / 3)
    if check[-1] == "0" and check[-2] == ".":
        return "Fizz"
    else:
        return str(num)

print(checkio(9))


# These "asserts" are used for self-checking
#assert checkio(15) == "Fizz"
#assert checkio(6) == "Fizz"
#assert checkio(10) == "10"
#assert checkio(7) == "7"