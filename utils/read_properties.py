import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class read_config:

    def get_base_URL(self):
        url = config.get("common info", "base_URL")
        return url

    def get_username(self):
        username = config.get("common info", "username")
        return username

    def get_password(self):
        password = config.get("common info", "password")
        return password