fizz = int(input("Введите первое число:\n"))
buzz = int(input("Введите второе число:\n"))
n = int(input("Введите третье число:\n"))

result = ""

for і in range(1, n + 1):
    if і % fizz == 0 and і % buzz == 0:
        result += "FB"
    elif і % fizz == 0:
        result += "F"
    elif і % buzz == 0:
        result += "B"
    else:
        result += str(і)

print(result)

fizz = int(input("Введите первое число:\n"))
buzz = int(input("Введите второе число:\n"))
n = int(input("Введите третье число:\n"))

result_w = ""
i=0
while i < n:
    i+=1
    if i % fizz == 0 and i % buzz == 0:
        result_w += "FB"
    elif i % fizz == 0:
        result_w += "F"
    elif i % buzz == 0:
        result_w += "B"
    else:
        result_w += str(i)

print(result_w)

print("result_w")