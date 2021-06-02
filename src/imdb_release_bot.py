from src.imdb_releases import ImdbReleases

class ImdbReleasesBot:
    def __init__(self, driver):
        self.driver = driver 
        self.url = f'https://www.imdb.com/calendar/'

    def get_movies_releases(self):
        self.driver.get(self.url)
        release = ImdbReleases(self.driver)
        releases = []
        for elem in release.get_releases():
            if elem.tag_name == "h4":
                releases.append({'date': elem.text, 'movies': []})
            elif elem.tag_name == "ul":
                movies_list = elem.find_elements_by_xpath(".//a")
                for el in movies_list:
                    releases[-1]['movies'].append({'name': el.text, 'link': el.get_attribute("href")})

        self.driver.close() 
        return releases

