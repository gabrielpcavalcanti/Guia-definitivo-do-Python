from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

wb = load_workbook("gabriel.xlsx")
ws = wb.active

# insert rows

ws.insert_rows(7)
ws.insert_rows(8)

# delete rows

ws.delete_rows(1)

# insert columns

ws.insert_cols(2)
ws.insert_cols(3)

# delete columns

ws.delete_cols(4)

wb.save("gabriel.xlsx")
