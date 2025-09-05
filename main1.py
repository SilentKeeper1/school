class Animal():
    def __init__ (self, kind, height, legs):
        self. kind = kind
        self. height = height
        self. legs = legs


k = input('Вид тварини')
h = int(input('Зріст'))
l = int(input('Кількість лап'))


a1 = Animal(k, h, l)


print( 'Вид – ', a1.kind, 'Зріст – ', a1.height, 'Лап – ', a1.legs)