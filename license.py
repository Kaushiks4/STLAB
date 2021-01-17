import openpyxl

wb = openpyxl.load_workbook('sheet.xlsx')  
sheet = wb.active

def search(licenseKey):
    flag = 0
    for row in sheet.iter_rows(min_row=1, min_col=1, max_row=10, max_col=4):  
        for cell in row:  
            if cell.value == licenseKey:
                for cell in row:
                    print(cell.value)
                flag = 1
    return flag

if __name__ == "__main__":
    licenseKey = input("Enter the 16 bit license key to be found")
    if len(licenseKey) < 16:
        print('Enter licenseKey of length 16')
    else:
        flag = search(licenseKey)
        if flag == 0:
            print('')
            print('License key not found!!')