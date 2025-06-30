class Employee:
    def __init__(self):
        self.name = "tabiq"        # public
        self._salary = 50000      # protected
        self.__ssn = "123-45-6789"  # private

emp = Employee()
print(emp.name)
print(emp._salary)
# print(emp.__ssn)  # Will raise AttributeError
print(emp._Employee__ssn)  # Accessing private using name mangling
