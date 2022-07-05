import time


class DateUtils:


    @staticmethod
    def delaySeconds(seconds):
        if(seconds > 0.0):
            print(f'Sleeping {seconds} seconds.')
            time.sleep(seconds)
