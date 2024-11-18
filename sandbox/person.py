
class Person:

    # initialization

    def __init__(self, name:str, residence:str) -> None:
        self.name = name
        self.residence = residence

    # methods

    def tell(self):
        print(f'Ik ben {self.name} en ik woon in {self.residence}.')

    def move(self, new_residence:str):
        self.residence = new_residence

    def __str__(self):
        return f'Person: {self.name}'


class Customer(Person):

    def tell(self):
        print(f'Ik ben een VIP klant {self.name} en ik woon in {self.residence}.')




# -----------------------------------------------

if __name__ == '__main__':

    p = Person('Peter', 'Lhee')
    p2 = Customer('Rkya', 'Barendrecht')

    print(type(p))
    print(p.name)
    print(p.residence)

    p.tell()

    p.move('Soesterberg')
    
    p.tell()

    p2.tell()

    print(p)
