class Phone:
    def __init__(self, phone_number=None):
        self.phone_number = phone_number  # Початковий номер телефону
        self.__counter_incoming_number = 0  # Захищене поле лічильника вхідних дзвінків

    def set_number(self, phone_number):
        self.phone_number = phone_number  # Метод для встановлення номера телефону

    def get_incoming_calls(self):
        return self.__counter_incoming_number  # Метод для отримання кількості вхідних дзвінків

    def receive_call(self):
        self.__counter_incoming_number += 1  # Метод для збільшення лічильника при прийнятті дзвінка

# Створення трьох різних об'єктів телефону
phone1 = Phone("123-456-7890")  # Початковий номер
phone2 = Phone("098-765-4321")  # Початковий номер
phone3 = Phone("555-123-4567")  # Початковий номер

# Прийняття дзвінків на кожному телефоні
phone1.receive_call()  # Два дзвінки на перший телефон
phone1.receive_call()
phone2.receive_call()  # Один дзвінок на другий телефон
phone3.receive_call()  # Три дзвінки на третій телефон
phone3.receive_call()
phone3.receive_call()

# Функція для повернення загальної кількості прийнятих дзвінків з усіх телефонів
def total_incoming_calls(phone_list):
    total_calls = 0
    for phone in phone_list:
        total_calls += phone.get_incoming_calls()  # Додаємо всі прийняті дзвінки
    return total_calls

# Загальна кількість прийнятих дзвінків з трьох телефонів
total_incoming_calls([phone1, phone2, phone3])  # Повертає загальну кількість дзвінків


