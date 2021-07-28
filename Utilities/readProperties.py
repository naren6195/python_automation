import configparser


config=configparser.RawConfigParser()
config.read(".\\Configuration/config.ini")

class ReadConfig():
    @staticmethod
    def getAppilicationUrl():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getusername():
        email=config.get('common info','username')
        return email
    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

