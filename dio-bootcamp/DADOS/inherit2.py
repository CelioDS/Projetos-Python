class Animal:
    def __init__(self, number_patas):
        self.number_patas = number_patas

    def __str__(self):
        return f"{self.__class__.__name__} {', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}\n"

class Mammal(Animal):
    def __init__(self, color, **KW):
        self.color = color
        super().__init__(**KW)

class Bird(Animal):
    def __init__(self,colorB, **KW,):
        self.colorB = colorB
        super().__init__(**KW)

class Gato(Mammal):
    pass

class Platypus(Mammal,Bird):
    def __init__(self,number_patas,color, colorB):
        print(Platypus.__nro__)
        super().__init__(number_patas=4,color='blue', colorB='a')

gato = Gato(number_patas=4,color='white')
plat = Platypus(number_patas=4,color='blue', colorB='a')

print(gato)
print(plat)


