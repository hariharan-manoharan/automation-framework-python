from appium import webdriver
import subprocess
import time
import os


fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class DriverScript:

    process = ''

    def __init__(self, port, desiredCap):
        self.port = port
        self.desiredCap = desiredCap
        print 'Android Driver Factory constructor is executed...'

    def setDriver(self):
        desired_caps = {}
        desired_caps['platformName'] = self.desiredCap.get('platformname')
        desired_caps['platformVersion'] = self.desiredCap.get('platformversion')
        desired_caps['deviceName'] = self.desiredCap.get('devicename')
        desired_caps['noReset'] = self.desiredCap.get('noreset')
        desired_caps['newCommandTimeout'] = self.desiredCap.get('newcommandtimeout')
        desired_caps['app'] = PATH(
            '../../../fulcrum/apkFiles/'+self.desiredCap.get('app')
        )
        remoteAddress = 'http://'+self.desiredCap.get('remote.host')+':'+self.port+'/wd/hub'
        self.driver = webdriver.Remote(remoteAddress, desired_caps)


    def getDriver(self):
        return self.driver

    def startAppiumServerInstance(self):
        self.process = subprocess.Popen(['appium','-p', self.port], shell=True)
        time.sleep(5)


    def killAppiumServerInstance(self):
        self.process.terminate()






