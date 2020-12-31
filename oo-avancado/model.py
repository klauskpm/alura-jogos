from abc import ABC


class VideoABC(ABC):
    def __init__(self, title, year):
        self._title = title.title()
        self.year = year
        self._likes = 0

    def __str__(self):
        return f'Título {self.title} - Ano {self.year} | likes {self.likes}'

    @property
    def title(self):
        return self._title

    @property
    def likes(self):
        return self._likes

    def like(self):
        self._likes += 1


class Movie(VideoABC):
    def __init__(self, title, year, duration):
        super().__init__(title, year)
        self.duration = duration

    def __str__(self):
        return f'Título {self.title}' \
               f' - Ano {self.year}' \
               f' - Duração {self.duration} minutos' \
               f' | likes {self.likes}'


class Series(VideoABC):
    def __init__(self, title, year, seasons):
        super().__init__(title, year)
        self.seasons = seasons

    def __str__(self):
        return f'Título {self.title}' \
               f' - Ano {self.year}' \
               f' - {self.seasons} temporadas' \
               f' | likes {self.likes}'


ving = Movie('vingadores: guerra infinita', 2018, 200)
ving.like()
ving.like()
print(ving.likes)

print(ving)