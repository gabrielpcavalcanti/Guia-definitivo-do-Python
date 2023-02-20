from openpyxl import Workbook, load_workbook

wb = load_workbook('grades.xlsx')
ws = wb.active
print(ws)

# give the value of a cell

print(ws['A3'].value)

# Change some value

ws["A1"] = 'test'

# Save the work

wb.save('grades.xlsx')

# Show all of the sheets in the excel file

print(wb.sheetnames)

# work with an expecifc sheet

# ws = wb['sheet 1'] for example

# Creating a new sheet 

wb.create_sheet("Test")

print(wb.sheetnames)