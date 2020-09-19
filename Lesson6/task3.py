class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


while True:
    try:
        wage_value = float(input('Enter wage: '))
        bonus_value = float(input('Enter bonus: '))
        break
    except ValueError:
        print('Enter float values')

worker_1 = Position(input('Enter name: '),
                    input('Enter second name: '),
                    input('Enter position: '),
                    wage_value,
                    bonus_value)

print(worker_1.name)
print(worker_1.surname)
print(worker_1.position)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
