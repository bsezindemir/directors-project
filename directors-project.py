class Director:

    yearOfDeath = "Still Alive"
    quote = "Sorry, s/he doesn't have a quote"
    award = "None"

    def __init__(self, Name, Movie, Year):
        self.Name = Name
        self.Movie = Movie
        self.Year = Year

    @classmethod
    def viewYearOfDeath(cls, year_of_death):
        cls.yearOfDeath = year_of_death
    
    def viewQuote(cls, _quote):
        cls.quote = _quote

    def viewAward(cls, _award):
        cls.award = _award

    def intro(self):
        return f"Director's;\nName: {self.Name}\nMovie: {self.Movie}\nRelease year of the movie: {self.Year}"

    def dQuote(self):
        return f"{self.Name}'s quote: {self.quote}"

    def doYouLike(self):
        response = input("Do you like this director? (y or n)\n")
        if response == "y":
            print("Good for you\n")
        if response == "n":
            print("Pity you\n")

director1 = Director("Alfred Hitchock", "Psycho", 1964)
director2 = Director("Stanley Kubrick", "A Clockwork Orange", 1971)
director3 = Director("Kátia Lund", "City of God", 2002)
director4 = Director("Christopher Nolan", "Dark Knight", 2008)
director5 = Director("Nuri Bilge Ceylan", "Kış Uykusu", 2014)
director6 = Director("Frank Derebont", "Shawshank Redemption", 1994)

director1.yearOfDeath  = 1980
director1.viewQuote("There is no terror in the bang, only the anticipation of it.")
director1.viewAward("Golden Globe - Best Supporting Actress")

director2.yearOfDeath = 1999
director2.viewQuote("If it can be written, or thought, it can be filmed.")
director2.viewAward("Venice Film Festival - Pasinetti")

director3.viewAward("Academy Award - Best Director")
director4.viewAward("Academy Award - Best Supporting Actor")
director5.viewAward("Cannes Film Festival - Palme d'Or")

import time

print(director1.intro())
print(f'Award: {director1.award}\nYear of death: {director1.yearOfDeath}')
print(director1.dQuote())
print(director1.doYouLike())
time.sleep(1)

print("\n")
print(director2.intro())
print(f'Award: {director2.award}\nYear of death: {director2.yearOfDeath}')
print(director2.dQuote())
print(director2.doYouLike())
time.sleep(1)

print("\n")
print(director3.intro())
print(f'Award: {director3.award}\nYear of death: {director3.yearOfDeath}')
print(director3.dQuote())
print(director3.doYouLike())
time.sleep(1)

print("\n")
print(director4.intro())
print(f'Award: {director4.award}\nYear of death: {director4.yearOfDeath}')
print(director4.dQuote())
print(director4.doYouLike())
time.sleep(1)

print("\n")
print(director5.intro())
print(f'Award: {director5.award}\nYear of death: {director5.yearOfDeath}')
print(director5.dQuote())
print(director5.doYouLike())
time.sleep(1)

print("\n")
print(director6.intro())
print(f'Award: {director6.award}\nYear of death: {director6.yearOfDeath}')
print(director6.dQuote())
print(director6.doYouLike())
time.sleep(1)
