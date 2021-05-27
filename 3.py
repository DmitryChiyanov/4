class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


persona = Position("Дима", 'Чиянов', "передвигатель коробочек", 99999999, 99999999)
print(persona.get_full_name())
print(persona.position)
print(persona.get_full_profit())