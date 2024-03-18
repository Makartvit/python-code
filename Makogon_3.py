with open('C:/Users/АРТЕМ/Desktop/fizz_bazz.txt', 'r') as file:
    fizz_bazz = file.read()

fizz_bazz_num = [int(num) for num in fizz_bazz.split()]

all_results = []

for i in range(0, len(fizz_bazz_num), 3):
    if i + 2 < len(fizz_bazz_num):
        fizz, buzz, n = fizz_bazz_num[i], fizz_bazz_num[i+1], fizz_bazz_num[i+2]

        result = []
        for num in range(1, n + 1):
            if num % fizz == 0 and num % buzz == 0:
                result.append("FB ")
            elif num % fizz == 0:
                result.append("F ")
            elif num % buzz == 0:
                result.append("B ")
            else:
                result.append(str(num) + " ")
        all_results.append(''.join(result))
        print(''.join(result))
    else:
        print("Конец")

with open('C:/Users/АРТЕМ/Desktop/fizz_bazz_rez.txt', 'w') as file:
    file.write('\n'.join(all_results))