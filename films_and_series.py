from faker import Faker

print("Biblioteka Filmów")

class Film:
    def __init__(self, title, publication_year, gentre):
        self.title = title
        self.publication_year = publication_year
        self.gentre = gentre
        
        self.number_of_watching = 0

    def play(self, step=1):
       self.number_of_watching += step

    def __str__(self):
        return f'{self.title} ({self.publication_year})'    

class Series(Film):
    def __init__(self, epizode_number, season_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.epizode_number = epizode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title} {self.epizode_number} {self.season_number}'     
    
film1 = Film(title = "Titanic", publication_year = 1995, gentre = "Drama")
film2 = Film(title = "Mask", publication_year = 1990, gentre = "Comedy")
series1 = Series(title = "BBT", publication_year = 2010, gentre = "Comedy", epizode_number = "2", season_number = "3")
series2 = Series(title = "Friends", publication_year = 1999, gentre = "Comedy", epizode_number = "4", season_number = "5")

print(series2)
films = [film1, film2]
get_films = sorted(films,key=lambda Film: Film.publication_year)
get_films()

