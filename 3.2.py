class Portugal:
    name = "Portugal"
    def City(self):
        print("Capital: Lisbon")
    def Population(self):
        print("Population: 10,280,000 คน")
    def Abbreviations(self):
        print("Abbreviations: Por")
class America:
    name = "America"
    def City(self):
        print("Capital: Washington D.C")
    def Population(self):
        print("Population: 328,200,000 คน")
    def Abbreviations(self):
        print("Abbreviations: USA")
class Germany:
    name = "Germany"
    def City(self):
        print("Capital: Berlin")
    def Population(self):
        print("Population: 83,020,000 คน")
    def Abbreviations(self):
        print("Abbreviations: GER")
class Russia:
    name = "Russia"
    def City(self):
        print("Capital: Moscow")
    def Population(self):
        print("Population: 143,020,000 คน")
    def Abbreviations(self):
        print("Abbreviations: Rus")

por = Portugal()
usa = America()
ger = Germany()
rus = Russia()

for country in (por, usa, ger, rus):
    print(country.name)
    country.City()
    country.Population()
    country.Abbreviations()
    print()