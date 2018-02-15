from com.fulcrum.automation.framework.reportFactory.StatusEnum import Status
from ..pageObjectRepository.CommonObjects import CommonObjects
from ..pageObjectRepository.HomePageObjects import PageObjects
from ..reusableLibrary.CommonFuntions import WebReusableFunctions

class WebCustomFunctions(WebReusableFunctions, PageObjects, CommonObjects):

    def __init__(self, driver, report):
        WebReusableFunctions.__init__(self, driver, report)
        PageObjects.__init__(self)
        CommonObjects.__init__(self)

    def click_client_folder(self):
        self.click_element_xpath(self.xpath_client_folder, "Client Folder")