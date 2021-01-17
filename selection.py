import xlrd
from records import createSpreadSheet

workbook = xlrd.open_workbook('records5.xlsx')
sheet = workbook.sheet_by_index(0)
data = {}

for row in range(sheet.nrows):
    data[row] = {}
    data[row]["Name"] = sheet.cell_value(row,0)
    data[row]["USN"] = sheet.cell_value(row,1)
    data[row]["m1"] = sheet.cell_value(row,2)
    data[row]["m2"] = sheet.cell_value(row,3)
    data[row]["m3"] = sheet.cell_value(row,4)

records = {}
i=0
for key in data:
    if int(data[key]["m1"]) < 30 or int(data[key]["m2"]) < 30 or int(data[key]["m3"]) < 30:
        record = {}
        record["Name"] = data[key]["Name"]
        record["USN"] = data[key]["USN"]
        record["m1"] = data[key]["m1"]
        record["m2"] = data[key]["m2"]
        record["m3"] = data[key]["m3"] 
        records[i] = record
        i += 1

createSpreadSheet(records,i)
