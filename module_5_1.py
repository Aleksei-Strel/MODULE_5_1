class HOUSE:
    def __init__(self, name, numb_f):
        self.name = name
        self.number_of_floor = numb_f

    def go_to(self, new_floor):
        if int(new_floor) > int(self.number_of_floor) or int(new_floor) < 1:
            print(f'Этажа № {new_floor} не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(int(floor))


h1 = HOUSE('Скала', 28)
h2 = HOUSE('Хрущ', 5)

print(h1.name, h1.number_of_floor)
print(h2.name, h2.number_of_floor)

h1.go_to(28)
h1.go_to(0)
h2.go_to(3)
h2.go_to(7)