class Car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        print(self.brand)

    def set_brand(self):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        print(self.brand)
    
    def set_color(self):
        print(self.color)

    def set_mileage(self):
        print(self.mileage)

    def get_mileage(self, a):
        a = self.mileage
        return a

# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = Car('Volvo', 'Blå', 1587)
a_car.get_brand()
a_car.set_color()
a_car.set_mileage()

b_car = Car('Lambourgini', 'Rosa', 10)
b_car.get_brand()
b_car.set_color()
b_car.set_mileage()

c_car = Car('Ferrari', 'Röd', 1000)
c_car.get_brand()
c_car.set_color()
c_car.set_mileage()

print("")
cars = [a_car, b_car, c_car]

for car in cars:
    print(car.brand)


