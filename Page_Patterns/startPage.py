from OOP.Utility import  

# Create object of Configuration class

config = ConfigParser

# To read data from config file
config.read("D:/Develop/Python_source/web_go/OOP/Conf_files/Config.cfg")

print(config.get("StartPage", "username"))

