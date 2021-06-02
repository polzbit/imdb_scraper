##################################################################################
#  scrape imdb.com for information about releases
##################################################################################
from selenium.webdriver.common.by import By
from src.imdb_locators import ImdbLocators

class ImdbReleases:
    def __init__(self, driver):
        self.driver = driver 
        self.release_list = self.driver.find_elements(By.XPATH, ImdbLocators.releases_table)

    def get_releases(self):
        return self.release_list