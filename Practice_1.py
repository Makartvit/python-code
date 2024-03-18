#n = int(input("Введите число:\n"))
#if n % 2==0:
#    print("число парное")
#    print("число не парное")

#n = int(input("Введите число:\n"))
#if n % 3==0 and n % 5 == 0 and n % 2 != 0 and n % 10 !=0:
#    print("Число удовлетворяет всем условиям")
#else:
#    print("Число не удовлетворяет всем условиям")

#n = int(input("Введите число:\n"))
#result = ""

#for i in range(1, n+1):
#    if n%i == 0:
#        result+=str(i) + ", "

#result=result[:-2]
#print("Делители числа", n, ":", result)

# n = int(input("Введите число: "))
#
# n_str = str(n)
#
# for i in range(len(n_str)):
#     digit = int(n_str[i])
#     multiplier = digit * 10 ** (len(n_str) - i - 1)
#     print("Разряд", digit, "с множителем", multiplier)