# Шахматный король ходит по горизонтали, вертикали и диагонали,
# но только на 1 клетку. Даны две различные клетки шахматной
# доски, определите, может ли король попасть с первой
# клетки на вторую одним ходом.
X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())
if X1 + 1 == X2 and (Y1 + 1 == Y2 or Y1 - 1 == Y2 or Y1 == Y2):
    print('YES')
elif X1 == X2 and (Y1 + 1 == Y2 or Y1 - 1 == Y2):
    print('YES')
elif X1 - 1 == X2 and (Y1 + 1 == Y2 or Y1 - 1 == Y2 or Y1 == Y2):
    print('YES')
else:
    print('NO')