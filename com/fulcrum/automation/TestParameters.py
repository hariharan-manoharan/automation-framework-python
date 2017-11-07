

class TestParameters:

    def __init__(self,testcaseId, testdescription, execute):
        self.testcaseId = testcaseId
        self.testdescription = testdescription
        self.execute = execute


    def getTestcaseId(self):
        return self.testcaseId

    def getTestDescription(self):
        return self.testdescription

    def getExecute(self):
        return self.execute