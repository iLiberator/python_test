total = 0
price = 100

pas1 = int(input('Возвраст пассажира 1:\n'))
pas2 = int(input('Возвраст пассажира 2:\n'))
pas3 = int(input('Возвраст пассажира 3:\n'))
pas4 = int(input('Возвраст пассажира 4:\n'))
pas5 = int(input('Возвраст пассажира 5:\n'))
test_list = [pas1, pas2, pas3, pas4, pas5]
count = 0
while count < len(test_list):
    count += 1
    if test_list[count - 1] < 3:
        continue
    if test_list[count - 1] > 3:
        total += price

print(total)