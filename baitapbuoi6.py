from abc import ABC, abstractmethod

# Lớp cha trừu tượng
class BankAccount(ABC):
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = balance   # private

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Số dư không hợp lệ!")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Nạp {amount} thành công.")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Rút {amount} thành công.")
        else:
            print("Không thể rút tiền. Số dư không đủ hoặc số tiền không hợp lệ.")

    def display_info(self):
        print(f"Số tài khoản: {self.account_number}")
        print(f"Chủ tài khoản: {self.owner_name}")
        print(f"Số dư: {self.get_balance()}")

    @abstractmethod
    def account_type(self):
        pass


# Tài khoản tiết kiệm
class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def account_type(self):
        return "Tài khoản tiết kiệm"

    def display_info(self):
        print(f"Loại tài khoản: {self.account_type()}")
        super().display_info()
        print(f"Lãi suất: {self.interest_rate}")


# Tài khoản thanh toán
class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance=0, overdraft_limit=500):
        super().__init__(account_number, owner_name, balance)
        self.overdraft_limit = overdraft_limit

    def account_type(self):
        return "Tài khoản thanh toán"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print(f"Rút {amount} thành công.")
        else:
            print("Vượt quá hạn mức cho phép.")

    def display_info(self):
        print(f"Loại tài khoản: {self.account_type()}")
        super().display_info()
        print(f"Hạn mức thấu chi: {self.overdraft_limit}")


# Chương trình chính
acc1 = SavingsAccount("TK001", "Bùi Ngọc Thịnh", 10000000, 0.06)
acc2 = CheckingAccount("TK002", "Lê Minh Hoàng", 2000, 500)

print("=== Thông tin tài khoản 1 ===")
acc1.display_info()
acc1.deposit(500)
acc1.withdraw(300)
print("Số dư sau giao dịch:", acc1.get_balance())

print("\n=== Thông tin tài khoản 2 ===")
acc2.display_info()
acc2.deposit(1000)
acc2.withdraw(2300)
print("Số dư sau giao dịch:", acc2.get_balance())