##################################################################################
#  scrape imdb.com for information about a title trailer
##################################################################################
from selenium.webdriver.common.by import By
from src.imdb_locators import ImdbLocators


class ImdbTrailer:
    def __init__(self, driver):
        self.driver = driver 
        self.duration = self.driver.find_element(By.XPATH, ImdbLocators.trailer_duration)
        self.fullscreen_btn = self.driver.find_element(By.XPATH, ImdbLocators.fullscreen_button)
        self.play_btn = self.driver.find_element(By.XPATH, ImdbLocators.play_button)

    def get_duration(self):
        return self.duration

    def get_fullscreen_btn(self):
        return self.fullscreen_btn

    def get_play_btn(self):
        return self.play_btn
