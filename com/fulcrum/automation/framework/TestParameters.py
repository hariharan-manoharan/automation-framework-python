

class TestParameters:

    def __init__(self, test_case_id, test_description, execute):
        self.test_case_id = test_case_id
        self.test_description = test_description
        self.execute = execute

    def get_test_case_id(self):
        return self.test_case_id

    def get_test_description(self):
        return self.test_description

    def get_execute(self):
        return self.execute
