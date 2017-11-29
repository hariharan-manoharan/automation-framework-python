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

    userName = "hariharanmanohar1"
    accessKey = "QKpXf9VFm4wJyPigci55"

    def __init__(self, desiredCap):
        self.desiredCap = desiredCap
        print 'Android Driver Factory constructor is executed...'

    def setDriver(self):

        desired_caps = {}
        remoteAddress = ''

        desired_caps['platformName'] = self.desiredCap.get('platformname')
        desired_caps['deviceName'] = self.desiredCap.get('devicename')
        desired_caps['noReset'] = self.desiredCap.get('noreset')
        desired_caps['newCommandTimeout'] = self.desiredCap.get('newcommandtimeout')
        desired_caps['resetKeyboard'] = self.desiredCap.get('resetKeyboard')
        desired_caps['unicodeKeyboard'] = self.desiredCap.get('unicodeKeyboard')

        if self.desiredCap.get('run.mode') == 'local':
            desired_caps['app'] = PATH(
                '../../../fulcrum/apkFiles/'+self.desiredCap.get('app')
            )
            desired_caps['platformversion'] = self.desiredCap.get('platformversion')
            remoteAddress = 'http://' + self.desiredCap.get('local.host') + ':' + self.desiredCap.get('local.port') + '/wd/hub'
        elif self.desiredCap.get('run.mode') == 'remote':
            desired_caps['app'] = self.desiredCap.get('app')
            desired_caps['os_version'] = self.desiredCap.get('platformversion')
            remoteAddress = 'http://' + self.userName + ':' + self.accessKey + '@hub-cloud.browserstack.com/wd/hub'


        self.driver = webdriver.Remote(remoteAddress, desired_caps)


    def getDriver(self):
        return self.driver

    def startAppiumServerInstance(self):
        self.process = subprocess.Popen(['appium','-p', self.port], shell=True)
        time.sleep(5)


    def killAppiumServerInstance(self):
        self.process.terminate()






