##################################################################################
#  scrape imdb.com for information 
##################################################################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.imdb_release_bot import ImdbReleasesBot
from src.imdb_charts_bot import ImdbChartsBot
from src.imdb_title_bot import ImdbTitleBot
from src.imdb_trailer_bot import TrailerBot
from src.imdb_enum import ChartType, SortType

class ImdbBot:
    def __init__(self):
        self.driver = None
        self.new_releases = self.get_releases()
        self.charts = self.get_chart()

    def set_driver(self, headless=True):
        if self.driver != None:
            self.driver.quit()
        option = Options()
        option.headless = headless     # False - show selenium process, True - selenium work in background
        self.driver = webdriver.Chrome(executable_path="E:\Programs\chromedriver\chromedriver.exe", options=option)
    
    def get_releases(self):
        self.set_driver(True)
        return ImdbReleasesBot(self.driver).get_movies_releases()

    def get_chart(self, chartType = ChartType.PopularMovies, sortType = SortType.Ranking):
        self.set_driver(True)
        return ImdbChartsBot(self.driver).get_chart(chart_type = chartType, sort_type = sortType)

    def get_title(self, title):
        self.set_driver(True)
        return ImdbTitleBot(self.driver).get_title(title)    # "https://www.imdb.com/title/tt9639470/"
    
    def watch_trailer(self, trailer):
        self.set_driver(False)
        TrailerBot(self.driver).watch_trailer(trailer)      # "https://www.imdb.com/video/vi1389281305"

