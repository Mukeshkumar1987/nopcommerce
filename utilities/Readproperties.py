import configparser

config = configparser.RawConfigParser()

config.read("C:\\Users\\mukes\\PycharmProjects\\non commerce\\configurations\\config.ini")



class Readconfig():

    @staticmethod
    def geturl():
        url = config.get('common info', 'Url')
        return url

    @staticmethod
    def getEmail():
        Email = config.get('common info', 'Email')
        return Email


    @staticmethod
    def getpassword():
        password = config.get('common info', 'Password')
        return password
