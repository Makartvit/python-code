import datetime


class Employee:
    year_now_1 = datetime.date.today().year

    def __init__(self, name, salary_one_working_day):
        self.name = name
        self.salary_one_working_day = salary_one_working_day

    def work(self):
        print("I come to the office")

    def __str__(self):
        return f"Position: {self.name}"

    def __lt__(self, other):
        return self.salary_one_working_day < other.salary_one_working_day

    def __le__(self, other):
        return self.salary_one_working_day <= other.salary_one_working_day

    def __eq__(self, other):
        return self.salary_one_working_day == other.salary_one_working_day

    def __gt__(self, other):
        return self.salary_one_working_day > other.salary_one_working_day

    def __ge__(self, other):
        return self.salary_one_working_day >= other.salary_one_working_day

    def check_salary(self, day, month):
        # Текущая дата
        year_now = datetime.date.today().year  # Определение года

        # Начальная и конечная дата расчета
        start_date = datetime.date(year_now, month, 1)  # Первый день месяца
        end_date = datetime.date(year_now, month, day)  # Указанный день в месяце

        # Подсчет рабочих дней
        wrk_days = 0
        current_day = start_date  # Начинаем с первого дня месяца

        while current_day <= end_date:  # Цикл от первого дня месяца до end_date

            # calendar.weekday(year, month, day) Повертає день тижня(«0» — понеділок "6"-неділя)
            # для року(1970–…), місяця(1–12), день(1 - 31).

            if current_day.weekday() < 5:  # Проверка, является ли день рабочим
                wrk_days += 1  # Если рабочий день, увеличиваем на +1 день

            # увеличение дня на 1 до end_date

            current_day += datetime.timedelta(days=1)

        # Расчет итоговой ЗП
        return self.salary_one_working_day * wrk_days


class Recruiter(Employee):

    def work(self):
        print("I come to the office and start to coding")

    def __str__(self):
        return f"Position: {self.name}"


class Developer(Employee):

    def __init__(self, name, salary_one_working_day, tech_stack):
        super().__init__(name, salary_one_working_day)  # от Employee
        self.tech_stack = tech_stack

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def work(self):
        print("I come to the office and start to hiring")

    def __str__(self):
        return f"Position: {self.name}"

    def __add__(self, other):
        new_name = self.name + ' ' + other.name

        # Объединение технологий через set
        new_tech_stack = list(set(self.tech_stack + other.tech_stack))

        #  макс ЗП
        new_salary = max(self.salary_one_working_day, other.salary_one_working_day)

        # Новый объект Developer
        return Developer(new_name, new_salary, new_tech_stack)


# help(datetime.date.weekday)

employee_1 = Employee("Jo", 1070)
employee_2 = Employee("Bob", 2500)

print(employee_1 < employee_2)
print(employee_1 > employee_2)
print(employee_1 >= employee_2)

developer_1 = Developer("Jo", 1556, ["Python", "SQL"])
developer_2 = Developer("Bob", 3456, ["Python"])


# print(developer_1 < developer_2)


employee_3 = Employee("Bob", 1)

end_day = 6
end_month = 5

#  расчет зарплаты с начала месяца до end_day
salary = employee_3.check_salary(end_day, end_month)
print(f"Зарплата за рабочие дни с 1 по {end_day}.{end_month} в {Employee.year_now_1} году: {salary} грн")

# dev_1 = Developer("Jo", 1350, ["Python", "JavaScript", "SQL"])
# dev_2 = Developer("Bob", 2100, ["Python", "Java", "Ruby"])
#
# new_dev = dev_1 + dev_2
#
# print("New name:", new_dev.name)
# print("Salary:", new_dev.salary_one_working_day)
# print("Stack:", new_dev.tech_stack)
