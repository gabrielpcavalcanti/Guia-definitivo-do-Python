from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

wb = load_workbook("gabriel.xlsx")
ws = wb.active

# create a spreedsheet

for row in range(1,11):
    for col in range(1,5):
        char = get_column_letter(col)
        print(ws[char + str(row)])
        print(ws[char + str(row)].value)
        ws[char + str(row)] = char + str(row)

wb.save("gabriel.xlsx")
