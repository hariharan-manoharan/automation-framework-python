from selenium import webdriver
import os


fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class DriverScript:

    driverConfig = ''

    def __init__(self, driverConfig):
        self.driverConfig = driverConfig
        print 'Browser Driver Factory constructor is executed...'

    def setDriver(self, browser):

        firefox_driver_path = os.path.join(parentDir, self.driverConfig.get('driver.firefox.path'))
        chrome_driver_path = os.path.join(parentDir, self.driverConfig.get('driver.chrome.path'))

        if browser == 'Firefox':
            self.driver = webdriver.Firefox(executable_path=firefox_driver_path);
            self.driver.maximize_window()

        elif browser == 'Chrome':
            self.driver = webdriver.Chrome(executable_path=chrome_driver_path);
            self.driver.maximize_window()

        else:
            print 'Type of browser should be Firefox or Chrome...Please enter valid Browser type'

    def getDriver(self):
        return self.driver





