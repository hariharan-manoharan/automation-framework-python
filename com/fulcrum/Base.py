import datetime
import errno
import os

from com.fulcrum.automation.framework.TestParameters import TestParameters
from com.fulcrum.automation.framework.driverFactory import BrowserDriverFactory
from com.fulcrum.automation.framework.utils.FrameworkConfig import FrameworkConfigParser

from com.fulcrum.automation.framework.Executor import ExecutorService
from com.fulcrum.automation.framework.driverFactory import AndroidDriverFactory
from com.fulcrum.automation.framework.reportFactory.HtmlReportGenerator import HtmlReport
from com.fulcrum.automation.framework.utils.ExcelUtils import ExcelRunManagerAccess

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)


class Base:

    driver = ''
    htmlReport = HtmlReport
    framework_config = {}
    total_test_instance_to_execute_clean = []
    browser_driver_factory = ''
    android_driver_factory = ''
    start_execution_start_time = ''
    start_execution_end_time = ''

    def __init__(self):

        print 'Base class constructor executed...'

    def execute(self):

        #try:
            self.set_execution_start_time()
            self.make_sure_path_exists('reports')
            self.get_framework_config()

            self.initialize_report()
            self. collect_test_instances()
            self.execute_test()
        #except:
            print 'Exception occurred in execute method'
        #finally:

            self.set_execution_end_time()
            self.generate_report()

    def get_framework_config(self):

        framework_configurations = FrameworkConfigParser()
        self.framework_config = framework_configurations.readConfig()

    def collect_test_instances(self):

        run_manager_access = ExcelRunManagerAccess(self.framework_config)
        test_instances = run_manager_access.get_run_manager_info('RunManager')
        total_test_cases_to_execute = len(test_instances)

        if total_test_cases_to_execute == 0:
            print 'No test case is marked with Execute = Yes'
        else:
            for i in range(total_test_cases_to_execute):
                test_parameters = TestParameters(test_instances[i]['TC_ID'], test_instances[i]['TEST_DESCRIPTION']
                                                 , test_instances[i]['EXECUTE'])
                self.total_test_instance_to_execute_clean.insert(i, test_parameters)

    def initialize_report(self):

        Base.htmlReport = HtmlReport(self.framework_config)

    def create_browser_driver_object(self):

        self.browser_driver_factory = BrowserDriverFactory.DriverScript(self.framework_config)
        self.browser_driver_factory.setDriver(self.framework_config.get('browser'))
        self.driver = self.browser_driver_factory.getDriver()

    def create_android_driver_object(self):

        self.android_driver_factory = AndroidDriverFactory.DriverScript(self.framework_config)
        #self.android_driver_factory.startAppiumServerInstance()
        self.android_driver_factory.setDriver()
        self.driver = self.android_driver_factory.getDriver()

    def execute_test(self):

        if len(self.total_test_instance_to_execute_clean) != 0:
            for i in range(len(self.total_test_instance_to_execute_clean)):
                if 'Web App' == self.framework_config.get('testing.type'):
                    self.create_browser_driver_object()
                elif 'Mobile App' == self.framework_config.get('testing.type'):
                    self.create_android_driver_object()
                executor = ExecutorService(self.framework_config, self.htmlReport, self.driver
                                           , self.total_test_instance_to_execute_clean[i])
                executor.get_keywords()
                executor.execute_keywords()
                self.quit_driver()

    def quit_driver(self):

        if 'Web App' == self.framework_config.get('testing.type'):
            self.driver.close()
        elif 'Mobile App' == self.framework_config.get('testing.type'):
            # self.androidDriverFactory.killAppiumServerInstance()
            self.driver.quit()

    def generate_report(self):
        total_time_delta = self.start_execution_end_time - self.start_execution_start_time
        self.htmlReport.generateReport(str(total_time_delta))

        # hours = totalTimeDelta.seconds / 3600
        # minutes = totalTimeDelta.seconds / 60
        # seconds = totalTimeDelta.seconds

        # self.htmlReport.generateReport(str(str(hours) + 'h ' + str(minutes) + 'm ' + str(seconds) + ' secs'))

    @staticmethod
    def make_sure_path_exists(path):

        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def set_execution_start_time(self):

        self.start_execution_start_time = datetime.datetime.now()

    def set_execution_end_time(self):

        self.start_execution_end_time = datetime.datetime.now()


if __name__ == '__main__':
    Base().execute()





