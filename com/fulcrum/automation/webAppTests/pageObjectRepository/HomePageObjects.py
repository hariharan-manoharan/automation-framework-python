

class PageObjects:

    def __init__(self):
        self.xpath_data_form = '//div[@class = \'nav-tree-item unselectable nav-tree-item-dataform\']' \
                               '/div[contains(text(),\'{}\')]'
