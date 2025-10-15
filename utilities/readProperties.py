import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commoninfo', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('commoninfo', 'username' )
        return username

    @staticmethod
    def getPassword():
        password = config.get('commoninfo', 'password')
        return password