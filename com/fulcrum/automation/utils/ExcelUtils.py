import io
import os
import openpyxl
from openpyxl.utils import coordinate_from_string, column_index_from_string

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)
run_manager_file_path = os.path.join(os.path.dirname(parentDir), 'RunManager.xls')
testdata_file_path = os.path.join(os.path.dirname(parentDir), 'TestData.xlsx')


class ExcelAccess:

    def __init__(self):
        self.workbook = openpyxl.load_workbook(testdata_file_path)
        self.worksheet = self.workbook.get_sheet_by_name('Keywords')

    def setMaxRow(self):
        self.totalRows = self.worksheet.max_row
        #print self.totalRows

    def setMaxColumn(self):
        self.totalColumns = self.worksheet.max_column
        #print self.totalColumns

    def getRowData(self, sheetName, currentTestcase='TESTCASE1'):

        data = {}

        worksheet = self.workbook.get_sheet_by_name(sheetName)
        columnNames = self.columnNames(worksheet)
        currentRow = self.getRowNumber(worksheet, currentTestcase)

        coulmnCounter = 0

        for row in worksheet.iter_cols(min_row=currentRow, min_col=1, max_row=currentRow, max_col=self.totalColumns):
            for cell in row:
                if cell.value != None:
                    data[columnNames[coulmnCounter]] = cell.value
                    coulmnCounter += 1
        print data


    def getRowNumber(self, worksheet, testcasename):

        currentRowNumber = 0

        for row in worksheet.iter_rows(min_row=2, min_col=1, max_row=self.totalRows, max_col=1):
            for cell in row:
                if cell.value == testcasename:
                    currentRowNumber = cell.row

        return currentRowNumber


    def columnNames(self, worksheet):

        columnNames = []

        for row in worksheet.iter_cols(min_row=1, min_col=1, max_row=1, max_col=self.totalColumns):
            for cell in row:
                columnNames.append(cell.value)
        return  columnNames

if __name__ == '__main__':
    ea = ExcelAccess()
    ea.setMaxRow()
    ea.setMaxColumn()
    ea.getRowData('Keywords')




