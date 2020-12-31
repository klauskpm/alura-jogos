from abc import ABC


class VideoABC(ABC):
    def __init__(self, title, year):
        self.title = title.title()
        self.year = year
        self.__likes = 0

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
