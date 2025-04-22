class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.total_rate = 0
        self.ratings = 0

    def rate(self, series_rate: int):
        self.ratings += 1
        self.total_rate += series_rate

    def average_rate(self):
        return self.total_rate / self.ratings

    def __str__(self):
        ratings = "no ratings"
        if self.ratings:
            average_points = self.average_rate()
            ratings = f"{self.ratings} ratings, average {average_points:.1f} points"
        return f"{self.title} ({str(self.seasons)} seasons) \
        \ngenres: {', '.join(self.genres)} \
        \n{ratings}"


def minimum_grade(rating: float, series_list: list):
    return [series for series in series_list if series.average_rate() > rating]


def includes_genre(genre: str, series_list: list):
    return [series for series in series_list if genre in series.genres]
