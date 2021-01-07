# Для данного числа n<100 закончите фразу “На лугу пасется...”
# одним из возможных продолжений: “n коров”, “n корова”,
# “n коровы”, правильно склоняя слово “корова”.
C = int(input())
tens = C // 10 - C // 100 * 10
if C % 10 == 0:
    print(C, 'korov')
elif (C % 10 == 1 or C % 10 == 2 or C % 10 == 3 or C % 10 == 4) and tens == 1:
    print(C, 'korov')
elif C % 10 == 1 and not tens == 1:
    print(C, 'korova')
elif C % 10 == 2 or C % 10 == 3 or C % 10 == 4:
    print(C, 'korovy')
else:
    print(C, 'korov')
