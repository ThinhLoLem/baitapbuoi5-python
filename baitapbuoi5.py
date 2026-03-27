from abc import ABC, abstractmethod

# 1. Class Employee
class Employee(ABC):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.__salary = salary   # private

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Lương không hợp lệ!")

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Base Salary: {self.get_salary()}")

    @abstractmethod
    def calculate_salary(self):
        pass


# 2. Class Developer
class Developer(Employee):
    def __init__(self, id, name, salary, programming_language, overtime_hours):
        super().__init__(id, name, salary)
        self.programming_language = programming_language
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        return self.get_salary() + self.overtime_hours * 200

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")
        print(f"Overtime Hours: {self.overtime_hours}")
        print(f"Total Salary: {self.calculate_salary()}")


# 3. Class Manager
class Manager(Employee):
    def __init__(self, id, name, salary, bonus):
        super().__init__(id, name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.get_salary() + self.bonus

    def display_info(self):
        super().display_info()
        print(f"Bonus: {self.bonus}")
        print(f"Total Salary: {self.calculate_salary()}")


# Chương trình chính
dev1 = Developer("D01", "Bùi Ngọc Thịnh", 5000, "Python", 10)
mgr1 = Manager("M01", "Lê Thuận Dương", 8000, 2000)

print("=== Thông tin Developer ===")
dev1.display_info()

print("\n=== Thông tin Manager ===")
mgr1.display_info()