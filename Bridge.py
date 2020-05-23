class PC:
    def home_pc(self, items):
        pass

    def gaming_pc(self, items):
        pass


class Budget_PC(PC):
    def home_pc_v1(self, items):
        print("This is a budget pc V1: ", items)

    def home_pc_v2(self, items):
        print("This is a budget pc V2: ", items)

class Gaming_PC(PC):
    def gaming_pc_v1(self, items):
        print("This is a gaming pc V1: ", items)

    def gaming_pc_v2(self, items):
        print("This is a gaming pc V2: ", items)

class Computer:
    def __init__(self, PC):
        self.pc = PC

    def display_description(self):
        pass

    def add_objects(self):
        pass


class Home_PC(Computer):
    def __init__(self, PC, objects):
        super().__init__(PC)
        self.objects = objects

    def display_description(self):
        self.pc.home_pc_v1(self.objects)

    def display_desc(self):
        self.pc.home_pc_v2(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


class Gaming(Computer):
    def __init__(self, PC, objects):
        super().__init__(PC)
        self.objects = objects

    def display_description(self):
        self.pc.gaming_pc_v1(self.objects)

    def display_desc(self):
        self.pc.gaming_pc_v2(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects

budget = Budget_PC()
gaming = Gaming_PC()

ram = 8
vram = 2
v1 = Home_PC(budget, f'AMD FX8350, RAM {ram} GB, nVidia GeForce 1050 Ti {vram} GB')
v1.display_description()
v2 = Home_PC(budget, f'AMD FX8350, RAM {ram+8} GB, nVidia GeForce 1050 Ti {vram+2} GB')
v2.display_desc()
print('---------------------------------------')
v3 = Gaming(gaming, f'Intel i7 9770, RAM {ram+24} GB, nVidia GeForce 1650 Ti {vram+4} GB')
v3.display_description()
v4 = Gaming(gaming, f'Intel i7 9770, RAM {ram+56} GB, nVidia GeForce 1650 Ti {vram+6} GB')
v4.display_desc()