class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

a = Bank()
b = Bank()
Bank.change_bank_name("MyBank")
print(a.bank_name, b.bank_name)
