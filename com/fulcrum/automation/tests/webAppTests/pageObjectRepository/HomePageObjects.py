

class PageObjects:

    def __init__(self):

        self.xpath_client_folder = '//div[@class = \'nav-tree-item-label\' and contains(text(),\'Client\')]'
        self.xpath_dataform_folder = '//div[@class = \'nav-tree-item-label\' and @style = \'padding-left: 20px;\' and contains(text(),\'{}\')]'
        self.xpath_data_form = '//div[@class = \'nav-tree-item unselectable nav-tree-item-dataform\']' \
                               '/div[contains(text(),\'{}\')]'


