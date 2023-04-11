# Робота з клієнтами:
# Створити клас для клієнта банку, з атрибутами екземпляра:
# Прізвище
# Ім“я
# По-батькові
# вік
# середня зарплата
# місце проживання
# поточна заборгованість
# Останні 2 параметри задайте «Київ» та 0, по замовчуванню.
# Додайте методи:
# для зміни заробітної плати
# для зміни заборгованості
# Додайте атрибут класу «загальна к-сть клієнтів» = 0
# Створіть 2 клієнтів, а також створіть методи для :
# друку  атрибуту «загальна к-сть клієнтів»,
# друку типу кожного екземпляру, адреси в пам“яті,
# порівняння екземпляра класу з іншим

class BankCustomer:
    total_customers = 0
    def __init__(self, first_name, last_name, name, age, earn, adres, credit):
        self.first_name = first_name
        self.last_mane = last_name
        self.name = name
        self.age = age
        self.earn = earn
        self.adres = adres
        self.credit = credit
        BankCustomer.total_customers += 1
    def re_earn(self, earn):
        self.earn = earn
    def re_credit(self, credit):
        self.credit = credit

user_first = BankCustomer('Stas', 'Zelinskyi', 'Olegovich', 39, 1000000, 'Kiyv', 0)
user_second = BankCustomer('Igor', 'Pupkin', 'Slavij', 21, 100, 'Kiyv', 0)
print(BankCustomer.total_customers)
print(user_first.first_name)