##################################################################################
#  scrape imdb.com for information about a title
##################################################################################
from selenium.webdriver.common.by import By
from src.imdb_locators import ImdbLocators
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class ImdbTitle:
    def __init__(self, driver):
        self.driver = driver
        try:
            self.title_name = self.driver.find_element(By.XPATH, ImdbLocators.title_name)
            self.subtitle = self.driver.find_elements(By.XPATH, ImdbLocators.subtitle)
            self.release_date = self.subtitle[-1]
            self.title_image = self.driver.find_element(By.XPATH, ImdbLocators.title_image)
            self.trailer_link = self.driver.find_element(By.XPATH, ImdbLocators.trailer_link)
            self.trailer_image = self.driver.find_element(By.XPATH, ImdbLocators.trailer_image)
            self.director = self.driver.find_element(By.XPATH, ImdbLocators.title_director)
            self.description = self.driver.find_element(By.XPATH, ImdbLocators.title_description)
            self.cast_table = self.driver.find_elements(By.XPATH, ImdbLocators.cast_table)
            self.alt = False
        except NoSuchElementException:
            self.title_name = self.driver.find_element(By.XPATH, ImdbLocators.alt_title_name)
            self.subtitle = self.driver.find_elements(By.XPATH, ImdbLocators.alt_subtitle)
            self.subtitle.append(None)
            self.release_date = self.driver.find_element(By.XPATH, ImdbLocators.alt_release)
            self.title_image = self.driver.find_element(By.XPATH, ImdbLocators.alt_title_image)
            self.trailer_link = self.driver.find_element(By.XPATH, ImdbLocators.alt_trailer_link)
            self.trailer_image = self.driver.find_element(By.XPATH, ImdbLocators.alt_trailer_image)
            self.director = self.driver.find_element(By.XPATH, ImdbLocators.alt_director)
            self.description = self.driver.find_element(By.XPATH, ImdbLocators.alt_description)
            self.cast_table = self.driver.find_elements(By.XPATH, ImdbLocators.alt_cast_table)
            self.alt = True
            print("Switch to alternative")

    def get_title_name(self):
        return self.title_name
    
    def get_title_ganeres(self):
        return self.subtitle[:-1]

    def get_release_date(self):
        return self.release_date

    def get_title_image(self):
        return self.title_image

    def get_trailer_image(self):
        return self.trailer_image

    def get_trailer_link(self):
        return self.trailer_link
    
    def get_director(self):
        return self.director

    def get_decription(self):
        return self.description

    def get_cast(self):
        cast = []
        if not self.alt:
            for c in self.cast_table:
                cast_name = c.find_elements_by_xpath(".//td")[1]
                cast.append(cast_name)
        else:
            cast = self.cast_table
        return cast