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


class Playlist:
    def __init__(self, nome, videos_list):
        self.nome = nome
        self._videos_list = videos_list

    def __getitem__(self, item):
        return self._videos_list[item]

    @property
    def list(self):
        return self._videos_list

    @property
    def size(self):
        return len(self._videos_list)


ving = Movie('vingadores: guerra infinita', 2018, 200)
tmoc = Series('todo mundo odeia o chris', 2000, 8)
jujutsu = Series('jujutsu no kaisen', 2000, 8)

ving.like()
ving.like()

tmoc.like()
tmoc.like()
tmoc.like()
tmoc.like()

weekend_playlist = PlayList2('Weekend', [ving, tmoc, jujutsu])
sorted_playlist = sorted(weekend_playlist, key=lambda video: video.likes, reverse=True)

for video in weekend_playlist:
    print(f"Video info {video}")
