from abc import ABC


class VideoABC(ABC):
    def __init__(self, title, year):
        self.__title = title.title()
        self.year = year
        self.__likes = 0

    @property
    def title(self):
        return self.__title

    @property
    def likes(self):
        return self.__likes

    def like(self):
        self.__likes += 1


class Movie(VideoABC):
    def __init__(self, title, year, duration):
        super().__init__(title, year)
        self.duration = duration


class Series(VideoABC):
    def __init__(self, title, year, seasons):
        super().__init__(title, year)
        self.seasons = seasons


ving = Movie('vingadores: guerra infinita', 2018, 200)
ving.like()
ving.like()
print(ving.likes)
ving.likes = 7
print(ving.likes)