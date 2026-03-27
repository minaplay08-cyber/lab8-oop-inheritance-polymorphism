"""
Лабораторная работа 8. ООП. Наследование и полиморфизм
"""

# Задача 1: Иерархия сотрудников
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        return f"{self.name} выполняет свою работу"
    
    def get_info(self):
        return f"Имя: {self.name}, Зарплата: {self.salary}"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def work(self):
        return f"{self.name} пишет код на {self.programming_language}"
    
    def write_code(self):
        return f"{self.name} пишет алгоритмы и решает технические задачи"
    
    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, Роль: Разработчик, Язык: {self.programming_language}"


class Designer(Employee):
    def __init__(self, name, salary, software):
        super().__init__(name, salary)
        self.software = software
    
    def work(self):
        return f"{self.name} создает дизайн в {self.software}"
    
    def design(self):
        return f"{self.name} проектирует пользовательские интерфейсы и прототипы"
    
    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, Роль: Дизайнер, Программа: {self.software}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size    def work(self):
        return f"{self.name} управляет командой из {self.team_size} человек"
    
    def manage(self):
        return f"{self.name} планирует задачи и контролирует выполнение проекта"
    
    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, Роль: Менеджер, Размер команды: {self.team_size}"


# Задача 2: Иерархия животных
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        return f"{self.name} издает звук"
    
    def move(self):
        return f"{self.name} перемещается"


class Mammal(Animal):
    def __init__(self, name, age, hair_color):
        super().__init__(name, age)
        self.hair_color = hair_color
    
    def make_sound(self):
        return f"{self.name} издает звук млекопитающего"
    
    def move(self):
        return f"{self.name} ходит или бегает"
    
    def feed_milk(self):
        return f"{self.name} кормит детенышей молоком"


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span
    
    def make_sound(self):
        return f"{self.name} поет или щебечет"
    
    def move(self):
        return f"{self.name} летает"
    
    def fly(self):
        return f"{self.name} расправил крылья размахом {self.wing_span} см и взлетел"


class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type
    
    def make_sound(self):
        return f"{self.name} не издает звуков (или издает звуки под водой)"
    
    def move(self):
        return f"{self.name} плавает в {self.water_type} воде"
    
    def swim(self):
        return f"{self.name} плавает в поисках пищи"


# Задача 3: Система уведомлений
class Notifier:
    def send(self, message):
        raise NotImplementedError("Метод send должен быть реализован в подклассе")


class EmailNotifier(Notifier):
    def __init__(self, email_address):
        self.email_address = email_address
    
    def send(self, message):
        return f"Отправка email на {self.email_address}: {message}"


class SMSNotifier(Notifier):
    def __init__(self, phone_number):
        self.phone_number = phone_number
    
    def send(self, message):
        return f"Отправка SMS на {self.phone_number}: {message}"


class PushNotifier(Notifier):
    def __init__(self, device_token):
        self.device_token = device_token
    
    def send(self, message):
        return f"Отправка push-уведомления на устройство {self.device_token}: {message}"


def notify_all(notifiers, message):
    results = []
    for notifier in notifiers:
        results.append(notifier.send(message))
    return results


# Демонстрация работы
def main():
    print("="*50)
    print("ЗАДАЧА 1: Иерархия сотрудников")
    print("="*50)
    
    # Создаем сотрудников
    employees = [
        Developer("Алексей", 150000, "Python"),
        Designer("Мария", 120000, "Figma"),
        Manager("Иван", 200000, 10)
    ]
    
    # Выводим информацию и работу каждого
    for emp in employees:
        print(emp.get_info())
        print(f"Работа: {emp.work()}")
        print("-"*50)
    
    print("\n" + "="*50)
    print("ЗАДАЧА 2: Иерархия животных")
    print("="*50)
    
    # Создаем животных
    animals = [
        Mammal("Лев", 5, "золотистый"),
        Bird("Орел", 3, 200),
        Fish("Карп", 2, "пресной")
    ]
    
    # Демонстрируем полиморфизм
    for animal in animals:
        print(f"{animal.name} ({type(animal).__name__}):")
        print(f"Звук: {animal.make_sound()}")
        print(f"Перемещение: {animal.move()}")
        print("-"*50)
    
    print("\n" + "="*50)
    print("ЗАДАЧА 3: Система уведомлений")
    print("="*50)
    
    # Создаем систему уведомлений
    notifiers = [
        EmailNotifier("minaplay08@gmail.com"),
        SMSNotifier("+7 777 77 77 77"),
        PushNotifier("qwerty_1234_")
    ]
    
    # Отправляем уведомления
    messages = notify_all(notifiers, "Привет! Это тестовое уведомление.")
    for msg in messages:
        print(msg)


if __name__ == "__main__":
    main()