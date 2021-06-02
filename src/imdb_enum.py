from enum import Enum

class SortType(Enum):
    Ranking = "Ranking"
    Rating = "IMDB Rating"
    Date = "Release Date"

class ChartType(Enum):
    TopMovies = "top"
    PopularMovies = "moviemeter"
    TopTv = "toptv"
    PopularTv = "tvmeter"