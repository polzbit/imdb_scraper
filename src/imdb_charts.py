##################################################################################
#  scrape imdb.com for information about charts
##################################################################################
from selenium.webdriver.common.by import By
from src.imdb_locators import ImdbLocators


class ImdbCharts:
    def __init__(self, driver):
        self.driver = driver
        self.sort_drop = self.driver.find_elements(By.XPATH, ImdbLocators.sort_dropdown)
        self.chart_table = self.driver.find_elements(By.XPATH, ImdbLocators.chart_table)

    def get_sort_dropdown(self):
        return self.sort_drop
    
    def get_chart_table(self):
        return self.chart_table
