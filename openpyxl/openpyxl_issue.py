# What is openpyxl? a python library to read and write excel files
# Error in openpyxl module:
# After you update a cell with a formula like =sum(1,2) and save it,
# the value of the fomula cell get disappeared after adjusting the data only option.
# In other words, it prints out None instead of 3. ß


import openpyxl as op

wb = op.Workbook()
ws = wb.active
ws['A1'] = 1
ws['B1'] = 2
ws['C1'] = '=sum(a1,b1)'
wb.save('sample.xlsx')
wb.close()
ws = op.load_workbook('sample.xlsx', data_only=True).active
cell = ws['a1:c1']
for row in cell:
    for r in row:
        print(r.value)
'''
1
2
None
'''
wb.close()
# ============================================================================
# Solutions: xlwings
import xlwings as xw

app = xw.App(visible=False)
wbx = app.books.open('sample.xlsx')
ws = wbx.sheets[0]
v = ws.range('C1').value
wbx.close()
app.kill()
