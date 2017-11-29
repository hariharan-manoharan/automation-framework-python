import os
from webAppTests.BusinessComponents import BusinessComp
from utils.ExcelUtils import ExcelTestDataAccess
from mobileAppTests.AppiumTestSuite import TestSuite1


fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)


class ExecutorService:

    keywords = {}
    arguments = {}

    def __init__(self, framework_config, report, driver, test_parameters):
        self.is_method_found = False
        self.framework_config = framework_config
        self.report = report
        self.driver = driver
        self.test_parameters = test_parameters
        print 'ExecutorService Constructor executed'

    def get_keywords(self):

        test_data_access = ExcelTestDataAccess(self.framework_config)
        self.keywords = test_data_access.get_row_data('Keywords', self.test_parameters.get_test_case_id())

    def execute_keywords(self):
        self.report.startTest(self.test_parameters.get_test_case_id(), self.test_parameters.get_test_description())
        for i in range(1, len(self.keywords)):

            current_keyword = self.keywords['KEYWORD_'+str(i)]

            self.report.addTestStep('Keyword', '<b>'+str(current_keyword).upper()+'</b>', 'INFO')

            if 'Web App' == self.framework_config.get('testing.type'):
                obj = BusinessComp(self.driver, self.report)
                names = dir(BusinessComp)
            elif 'Mobile App' == self.framework_config.get('testing.type'):
                obj = TestSuite1(self.driver, self.report)
                names = dir(TestSuite1)

            for name in names:
                attr = getattr(obj, name)
                if callable(attr) and name == current_keyword and not self.is_method_found:
                    self.is_method_found = True
                    attr()
                    if self.is_method_found:
                        self.report.addTestStep('Keyword', current_keyword + ' is executed successfully', 'INFO')
                        self.is_method_found = False
                    else:
                        self.report.addTestStep('Keyword', current_keyword + ' is executed successfully', 'INFO')
        self.report.endTest()
        self.report.generateReportImmediateFlush()