from src.imdb_title import ImdbTitle

class ImdbTitleBot:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self, link):
        self.driver.get(link)
        # get title name and ganeres
        title = ImdbTitle(self.driver)
        title_name =  title.get_title_name().text
        ganeres_elm = title.get_title_ganeres()
        ganeres = []
        for elm in ganeres_elm:
            ganeres.append(elm.text)
        # get title image and release date
        title_img = title.get_title_image().get_attribute("src")
        release_date = title.get_release_date().text
        # get trailer info
        trailer_link = title.get_trailer_link().get_attribute("href")
        trailer_img = title.get_trailer_image().get_attribute("src")
        # get title description
        description = title.get_decription().text
        director = title.get_director().text
        # get title cast
        cast_list = title.get_cast()
        cast = []
        for c in cast_list:
            cast.append(c.text)

        title = {
            'name': title_name,
            'decription': description,
            'director': director,
            'release_date': release_date,
            'image' : title_img,
            'ganeres': ganeres,
            'cast': cast,
            'trailer_image': trailer_img,
            'trailer': trailer_link
        }
        self.driver.close() 
        return title
