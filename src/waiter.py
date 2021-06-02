from threading import Thread
from time import sleep

class Waiter(Thread):   
    def __init__(self, timeout):
        super().__init__()
        self.timeout = timeout
        self.exit = False

    def stop(self):
        self.exit = True

    def run(self):
        for i in range(0, self.timeout):
            if self.exit: 
                print(i)
                break
            sleep(1)