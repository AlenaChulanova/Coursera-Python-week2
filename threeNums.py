# Дано три числа. Упорядочите их в порядке неубывания.
# Программа должна считывать три числа a,b,c, затем
# программа должна менять их значения так, чтобы стали
# выполнены условия a≤b≤c, затем программа выводит тройку a,b,c
A, B, C = int(input()), int(input()), int(input())
# abc
if A <= B <= C:
    print(A, B, C)
# acb
elif A <= C <= B:
    (C, B) = (B, C)
    print(A, B, C)
# bac
elif B <= A <= C:
    (A, B) = (B, A)
    print(A, B, C)
# bca
elif B <= C <= A:
    (A, C) = (C, A)
    (B, A) = (A, B)
    print(A, B, C)
# cab
elif C <= A <= B:
    (A, B) = (B, A)
    (A, C) = (C, A)
    print(A, B, C)
# cba
elif C <= B <= A:
    (A, C) = (C, A)
    print(A, B, C)
