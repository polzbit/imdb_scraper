from src.imdb_trailer import ImdbTrailer
from src.waiter import Waiter

class TrailerBot():
    def __init__(self, driver):
        self.driver = driver

    def watch_trailer(self, link):
        self.driver.get(link)
        self.driver.maximize_window() 
        trailer = ImdbTrailer(self.driver)
        # get duration
        dur = trailer.get_duration().text.split(":")
        time_length = 0
        if len(dur) == 2:
            time_length = int(dur[0]) * 60 + int(dur[1])
        elif len(dur) == 3:
            time_length = int(dur[0]) * 60 * 60 + int(dur[1]) * 60 + int(dur[2])
        # open in full screen
        trailer.get_fullscreen_btn().click()
        # play
        trailer.get_play_btn().click()
        # wait until video is finish or KeyboardInterrupt
        try:
            wait_thread = Waiter(time_length)
            wait_thread.daemon=True
            wait_thread.run()
        except (KeyboardInterrupt, SystemExit):
            wait_thread.stop()

        self.driver.close() 