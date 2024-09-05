class Person():
    def __init__ (self, name, lastname):
        self.name = name
        self.lastname = lastname

    def change_color (self, color):
        self.eyescolor = color

    def say_hello (self):
        print (f"hola, yo soy {self.name}")


person_1 = Person("soraya","henriquez")
print (person_1.name, person_1.lastname)

person_2 = Person("bethania", "mahotier")
print (person_2.name, person_2.lastname)

person_1.change_color("brown")
person_2.change_color("green")

print (person_1.eyescolor)
print (person_2.eyescolor)

person_1.say_hello()
person_2.say_hello()