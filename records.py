from xlwt import Workbook

def createSpreadSheet(records,len):
    workbook = Workbook()
    sheet = workbook.add_sheet('Sheet A')
    for i in range(len):
        sheet.write(i,0,records[i]["Name"])
        sheet.write(i,1,records[i]["USN"])
        sheet.write(i,2,records[i]["m1"])
        sheet.write(i,3,records[i]["m2"])
        sheet.write(i,4,records[i]["m3"])
    workbook.save('records' + str(len) + '.xlsx') 



if __name__ == "__main__":
    records = {}
    for i in range(5):
        data = {}
        data["Name"] = input("Enter the name of student " + str((i+1)) + " ")
        data["USN"] = input("Enter the USN of student " + str((i+1)) + " ")
        data["m1"] = input("Enter the Marks 1 of student " + str((i+1)) + " ")
        data["m2"] = input("Enter the Marks 2 of student " + str((i+1)) + " ")
        data["m3"] = input("Enter the Marks 3 of student " + str((i+1)) + " ")
        records[i] = data
    createSpreadSheet(records,5)

    

