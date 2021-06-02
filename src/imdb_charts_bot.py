from src.imdb_charts import ImdbCharts
from src.imdb_enum import ChartType, SortType

class ImdbChartsBot:
    def __init__(self, driver):
        self.driver = driver

    def get_chart(self, chart_type = ChartType.PopularMovies, sort_type = SortType.Ranking):
        my_url = f'https://www.imdb.com/chart/{chart_type.value}' 
        self.driver.get(my_url)
        self.driver.maximize_window()
        charts = ImdbCharts(self.driver)
        # find sort dropdown
        sort_drop = charts.get_sort_dropdown()
        for s in sort_drop:
            if s.text == sort_type.value:
                s.click()
                break

        # find movies table
        page_list = charts.get_chart_table()
        chart = []
        for tr in page_list:
            col_list = tr.find_elements_by_xpath(".//td")
            img_link = col_list[0].find_element_by_xpath(".//a/img").get_attribute("src")
            link = col_list[1].find_element_by_xpath(".//a").get_attribute("href")
            name = col_list[1].find_element_by_xpath(".//a").text
            year = col_list[1].find_element_by_xpath(".//span[contains(@class, 'secondaryInfo')]").text
            rank = col_list[2].text
            chart.append({'name': name, 'release': year, 'rank': rank,'img': img_link, 'link': link})

        self.driver.close() 
        return chart