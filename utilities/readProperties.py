import configparser
import os.path
# CONFIG_FILE_PATH = "C:\\Users\\rasul\\PycharmProjects\\pythonProject\\OpencartV1\\pythonProject1\\configurations\\config.ini"

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = (config.get('commonInfo', 'baseURL'))
        return url

    @staticmethod
    def getUserEmail():
        userName = (config.get('commonInfo', 'email'))
        return userName

    @staticmethod
    def getPassword():
        password = (config.get('commonInfo', 'password'))
        return password




