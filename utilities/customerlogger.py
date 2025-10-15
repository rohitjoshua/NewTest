import logging
import os


class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
        logging.basicConfig(filename=path,
                            format = '%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logger1 = logging.getLogger()
        logger1.setLevel(logging.DEBUG)
        return logger1



