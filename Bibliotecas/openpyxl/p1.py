from openpyxl import Workbook, load_workbook

wb = load_workbook('grades.xlsx')
ws = wb.active
print(ws)
