from openpyxl import Workbook, load_workbook

# Creating a new spredsheet

wb = Workbook()
ws = wb.active
ws.title = "Data"

# Put date inside the spredsheet

ws.append(['I', 'am', 'am','amazing'])
ws.append(['I', 'am', 'am','amazing'])
ws.append(['I', 'am', 'am','amazing'])
ws.append(['I', 'am', 'am','amazing'])
ws.append(['I', 'am', 'am','amazing'])
ws.append(['end'])


# Save the spredsheet

wb.save('gabriel.xlsx')
