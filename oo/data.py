class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def format_data(self):
        print(self.day, self.month, self.year, sep="/")