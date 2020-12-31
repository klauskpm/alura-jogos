from abc import ABC


class VideoABC(ABC):
    def __init__(self, title, year):
        self._title = title.title()
        self.year = year
        self._likes = 0

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


class Series(VideoABC):
    def __init__(self, title, year, seasons):
        super().__init__(title, year)
        self.seasons = seasons


ving = Series('vingadores: guerra infinita', 2018, 200)
ving.like()
ving.like()
print(ving.likes)