from openpyxl import Workbook

#with open('excel_test01','w+',encoding='utf-8') as f:

wb = Workbook()
wb.create_sheet('123')

print(wb.active)