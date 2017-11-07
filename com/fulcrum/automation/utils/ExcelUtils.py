import os
import openpyxl


fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)
run_manager_file_path = os.path.join(os.path.dirname(parentDir), 'RunManager.xlsx')
testdata_file_path = os.path.join(os.path.dirname(parentDir), 'TestData.xlsx')


class ExcelTestDataAccess:

    def __init__(self):
        self.workbook = openpyxl.load_workbook(testdata_file_path)

    def getWorkSheetObj(self, sheetName):
        return self.workbook.get_sheet_by_name(sheetName)

    def getMaxRow(self, worksheet):
        return worksheet.max_row

    def getMaxColumn(self, worksheet):
        return worksheet.max_column

    def getRowData(self, sheetName, currentTestcase):

        worksheet = self.getWorkSheetObj(sheetName)
        totalRows = self.getMaxRow(worksheet)
        totalColumns = self.getMaxColumn(worksheet)

        data = {}

        columnNames = self.getColumnNames(worksheet, totalColumns)
        currentRow = self.getRowNumber(worksheet, totalRows, currentTestcase)

        coulmnCounter = 0

        for row in worksheet.iter_cols(min_row=currentRow, min_col=1, max_row=currentRow, max_col=totalColumns):
            for cell in row:
                if cell.value != None:
                    data[columnNames[coulmnCounter]] = cell.value
                    coulmnCounter += 1
        #print data
        return data


    def getRowNumber(self, worksheet, totalRows, testcasename):

        currentRowNumber = 0

        for row in worksheet.iter_rows(min_row=2, min_col=1, max_row=totalRows, max_col=1):
            for cell in row:
                if cell.value == testcasename:
                    currentRowNumber = cell.row

        return currentRowNumber


    def getColumnNames(self, worksheet , totalColumns):

        columnNames = []

        for row in worksheet.iter_cols(min_row=1, min_col=1, max_row=1, max_col=totalColumns):
            for cell in row:
                columnNames.append(cell.value)
        return  columnNames


class ExcelRunManagerAccess:

    def __init__(self):
        self.workbook = openpyxl.load_workbook(run_manager_file_path)

    def getWorkSheetObj(self, sheetName):
        return self.workbook.get_sheet_by_name(sheetName)

    def getMaxRow(self, worksheet):
        return worksheet.max_row

    def getMaxColumn(self, worksheet):
        return worksheet.max_column

    def getRunManagerInfo(self, sheetName):

        worksheet = self.getWorkSheetObj(sheetName)
        totalRows = self.getMaxRow(worksheet)
        totalColumns = self.getMaxColumn(worksheet)

        runinfo = []

        columnNames = self.getColumnNames(worksheet, totalColumns)
        coulmnCounter = 0
        rowCounter = 0

        for row in worksheet.iter_rows(min_row=2, min_col=1, max_row=totalRows, max_col=totalColumns):
            rowdata = {}
            for cell in row:
                if cell.value != None:
                    rowdata[columnNames[coulmnCounter]] = cell.value
                    coulmnCounter += 1
            coulmnCounter = 0
            if rowdata['EXECUTE'] != 'No':
                runinfo.insert(rowCounter,rowdata)
                rowCounter += 1


        #print runinfo
        return runinfo


    def getColumnNames(self, worksheet , totalColumns):

        columnNames = []

        for row in worksheet.iter_cols(min_row=1, min_col=1, max_row=1, max_col=totalColumns):
            for cell in row:
                columnNames.append(cell.value)
        return  columnNames


if __name__ == '__main__':
    ea = ExcelTestDataAccess()
    ea.getRowData('Keywords', 'TESTCASE3')

    em = ExcelRunManagerAccess()
    testinstances = em.getRunManagerInfo('RunManager')
    totalTestcasesToExecute = len(testinstances)
    if totalTestcasesToExecute == 0:
        print 'No testcase is marked with Execute = Yes'
    else:
        print testinstances
        for i in range(totalTestcasesToExecute):
            testcaseId = testinstances[i]['TC_ID']
            testdescription = testinstances[i]['TEST_DESCRIPTION']
            execute = testinstances[i]['EXECUTE']
            print testcaseId +':'+testdescription+':'+execute







