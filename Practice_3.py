num = int(input("Введите положительное нечетное число: "))
# if num % 2 == 0 or num < 0:
#     print("Введите положительное нечетное число")
# else:
#     for i in range(1, num+1, 2):
#         print(" " * ((num - i)//2) + "*" * i)
#     for i in range(num - 2, 0, -2):
#         print(" " * ((num - i)//2) + "*" * i)

# file_test = "C:/Users/АРТЕМ/Desktop/pyt.txt"
#
# with open(file_test, "r") as file:
#     for line in file:
#         nums_do, nums_posle = line.strip().split(';')
#         nums_do = list(map(int, nums_do.split()))
#         nums_posle = list(map(int, nums_posle.split()))
#
#         if len(nums_do) > 0:
#             sum_nums_do = sum(nums_do)
#             a_nums_do = sum_nums_do / len(nums_do)
#         else:
#             sum_nums_do = 0
#         if len(nums_posle) > 0:
#             print(line.strip(), a_nums_do == int(a_nums_do) and True)
#         else:
#             print(line.strip(), False)


# kvartira = int(input("Введите номер квартиры: "))
# etazhey = int(input("Введите количество этажей: "))
# kvartir_na_etazhe = int(input("Введите количество квартир на этаже: "))
#
# podjezd = (kvartira - 1) // kvartir_na_etazhe + 1
# etazh = ((kvartira - 1) // kvartir_na_etazhe) % etazhey + 1
#
# print(f"Квартира №{kvartira} находится в {podjezd}-ом подъезде на {etazh}-ом этаже.")