class Lada():
    def __init__(self,*args,**kwargs):
        self.model = 'Niva'
        self.power = 89
        self.legit = True
        self.price = kwargs.get('price',0)
        self.color = kwargs.get('color','rust')
    def start(self):
        print('Engine started')
    def __str__(self):
        return f'Sergey Oil love {self.model}'

class Tuning(Lada):
    def stage(self):
        self.power += 100
        print(f' Your power now {self.power}')
    def __str__(self):
        print(f'Sergey Oil dizlike {self.model}')
    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.damage = '50%'

my_car = Tuning()

my_car.stage()
my_car.__str__()
print(my_car.damage)
