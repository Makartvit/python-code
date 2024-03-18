# def lower_case(case):
#     return case.lower()
#
# def upper_case(case):
#     return case.upper()
#
# case = list(input("Vedite text:"))
# list_1 = ["Vedite", "Text", "Plz"]
#
# case_1 = (map(upper_case, case))
# rez = " "
# for i in case_1:
#     rez += i
#
# print(rez)
#
# rez_1 = " "
# case_2 = (map(lower_case, case))
# for i in case_2:
#     rez_1 += i
#
# print(rez_1)
#
# case_3 = " ".join((map(upper_case, list_1)))
#
# print(case_3)


# def square(x):
#     return x**2
#
# def prime_number(x):
#     if x < 2:
#         return False
#     for i in range(2, int(x ** 0.5)+1):
#         if x % i == 0:
#             return False
#     return True
#
# n = list(range(60))
#
# prime = list(filter(prime_number, n))
#
# print(prime)
#
# in_square = list(map(square, prime))
#
# print(in_square)

# with open('C:/Users/АРТЕМ/Desktop/text.txt', 'r') as file:
#     text = file.read().replace('?', '').replace('.', '').replace(',', '').replace(';', '').split()
# print(text)
#
# def lower_case(case):
#     return case.lower()
#
# text_lower =list(map(lower_case, text))
#
# print(text_lower)
#
# number_of_each_word = {}
#
# for i in text_lower:
#     if i in number_of_each_word:
#         number_of_each_word [i] += 1
#     else:
#         number_of_each_word[i] = 1
#
# print(number_of_each_word)
#
# sorted_number_of_each_word = sorted(number_of_each_word.items())
#
# for i, j in sorted_number_of_each_word:
#     print(f"{i}: {j}")


def zip_1(l1, l2, l3, l4):
    list_123 = []
    min_1 = min(len(l1), len(l2), len(l3), len(l4))
    for i in range(min_1):
        list_123.append((l1[i], l2[i], l3[i], l4[i]))
    return list_123

list_1 = [11, 12, 13, 10, 12]
list_2 = ["ba", "ba", "co", "af"]
list_3 = [True, False, True, False]
list_4 = [True, "ba", 1, False]
list_5 = [True, "ba"]

res = zip_1(list_1, list_2, list_3, list_4)
print(res)

def zip_2(*many_lists_in_a_tuple):
    min_2 = min(len(list_6) for list_6 in many_lists_in_a_tuple)
    return [tuple(list_6[i] for list_6 in many_lists_in_a_tuple) for i in range(min_2)]

res_1= list(zip_2(list_1, list_2, list_3, list_4,list_5))
print(res_1)