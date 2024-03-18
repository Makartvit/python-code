# students = {
#     "Alice Ihan": [90, 70, 80, 50, 100],
#     "Bobito Trun" : [85, 70, 0, 80, 50],
#     "Cha Li" : [60, 70, 80, 50,100],
#     "Roma Vatan" : [90, 80, 80, 55, 0],
#     "Lima Tan" : [90, 70, 100, 50, 100],
# }
#
# successful_student = ''
# sunsuccessful_student = ''
#
# max_result = 0
# min_result = 100
#
# for student_name, student_grades in students.items():
#     grade_avg = sum(student_grades) / len(student_grades)
#     if grade_avg > max_result:
#         max_result = grade_avg
#         successful_student = student_name
#     elif grade_avg < min_result:
#         min_result = grade_avg
#         sunsuccessful_student = student_name
#
# print(f"Successful student: {successful_student} - Grade point average - {max_result}")
# print(f"Sunsuccessful student: {sunsuccessful_student} - Grade point average - {min_result}")



# students = {
#     "Alice Ihan": ["FrontEnd"],
#     "Bobito Trun" : ["Java"],
#     "Cha Li" : ["Python", "Java" "FrontEnd"],
#     "Roma Vatan" : ["Java", "FullStack"],
#     "Lima Tan" : ["Python", "Java", "FullStack"],
#     "Bobito Lima" : ["Python"]
# }
#
#
# students_in_group_Python = []
# students_in_group_Python_Java = []
# students_in_group_two_or_more = []
#
# for student, groups in students.items():
#     if "Python" in groups:
#         students_in_group_Python.append(student)
#     elif "Python" and "Java"  in groups:
#         students_in_group_Python_Java.append(student)
#     if len(groups) > 1:
#         students_in_group_two_or_more.append(student)
#     continue
#
#
# print("Students in group Python:", students_in_group_Python)
# print("Students in group Python and Java:", students_in_group_Python_Java)
# print("Students in group two or more:", students_in_group_two_or_more)

size = {
    "S": {"Ukraine": 46, "Germany": 40, "USA": 12, "United Kingdom": 28, "France": 42},
    "M": {"Ukraine": 48, "Germany": 42, "USA": 14, "United Kingdom": 30},
    "L": {"Ukraine": 50, "Germany": 44, "USA": 16, "United Kingdom": 32},
    "XL" : {"Ukraine": 52, "Germany": 46, "USA": 18, "United Kingdom": 34}
}

international_size = input("Введите международний женский размер - S, M, L, XL: ")
state_size = input("Введите страну - Ukraine, Germany, USA, United Kingdom: ")

def size_conversion(size_d, international_size, state_size):
    if international_size in size_d and state_size in size_d[international_size]:
        return size_d[international_size][state_size]
    else:
        return "Попробуйте снова"

box_size = size_conversion(size,international_size,state_size)

print(f"Перевод женского размера {international_size} для страны {state_size}:", box_size)