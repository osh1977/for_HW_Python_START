# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
# '''

# n = int(input("Введите n "))
# a = n // 100
# b = n % 100 // 10
# c = n % 10
# print(a+b+c)


a = int(input("Введите трёхзначное число "))
print(a//100 + a//10 % 10 + a % 10)

# a = 100
# print(a//100 + a//10%10 + a%10)
