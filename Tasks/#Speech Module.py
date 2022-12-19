#Speech Module

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"


def checkio(num: int) -> str:
    if num in range(1, 10):             # 1-9
        return FIRST_TEN[num - 1]
    if num in range(10, 20):            # 10-19
        return SECOND_TEN[num - 10]

    if num in range(20, 100, 10):       # 20-30-40 ... 80-90
        first_num = str(num)[0]
        return OTHER_TENS[int(first_num) - 2]
    
    if num in range(21, 100) and (num / 10) != int(str(num)[0]):        #21-29, 31-39, 41-49, 51-59 ... 91-99
        first_num = str(num)[0]
        last_num = str(num)[1]
        return f'{OTHER_TENS[int(first_num) - 2]} {FIRST_TEN[int(last_num) - 1]}'

    if num in range(100, 1000, 100):        #100-200-300 ... 800-900
        first_num = str(num)[0]
        return f'{FIRST_TEN[int(first_num) - 1]} {HUNDRED}'

    if num in range(110, 910, 100):                              #110, 210, 310, 410 ... 910
        first_num = str(num)[0]
        return f'{FIRST_TEN[int(first_num) - 1]} {HUNDRED} and {SECOND_TEN[0]}'

    if num in range(120, 1000, 10) and str(num)[-1] == '0':     #120, 130, 140 ... 980, 990
        first_num = str(num)[0]
        last_two_num = str(num)[1]
        return f'{FIRST_TEN[int(first_num) - 1]} {HUNDRED} {OTHER_TENS[int(last_two_num) - 2]}'

    if len(str(num)) == 3 and str(num)[1] == '0':        #101-109, 201-209, 301-309 ... 901-909
        first_num = str(num)[0]
        last_num = str(num)[2]
        return f'{FIRST_TEN[int(first_num) - 1]} {HUNDRED} {FIRST_TEN[int(last_num) - 1]}'

    
    if len(str(num)) == 3 and str(num)[1] == '1':            #111-119, 211-219, 311-319 ... 911-919
        first_num = str(num)[0]
        last_two_num = str(num)[-1]
        return f'{FIRST_TEN[int(first_num) - 1]} {HUNDRED} {SECOND_TEN[int(last_two_num)]}'

    if len(str(num)) == 3 and int(str(num)[1]) in range(2, 10):     #120, 130, 140 ... 980, 990
        first_num = str(num)[0]
        mid_num = str(num)[1]
        last_num = str(num)[-1]
        return f'{FIRST_TEN[int(first_num) - 1]} {HUNDRED} {OTHER_TENS[int(mid_num) - 2]} {FIRST_TEN[int(last_num) - 1]}'


print(checkio(302))

