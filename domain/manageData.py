import gspread
import authentication

def getList():
    json_file_name = 'finddomain-265318-8ac51b66da62.json'
    credential = authentication.authenticate(json_file_name)
    gc = gspread.authorize(credential)
    wks = gc.open("domainTest").sheet1

    values_list = wks.col_values(1)
    return values_list


def writeList(value_list):
    json_file_name = 'finddomain-265318-8ac51b66da62.json'
    credential = authentication.authenticate(json_file_name)
    gc = gspread.authorize(credential)
    wks = gc.open("domainTest").sheet1

    cell_list = wks.range('F1:F10')

    index = 0
    for cell in cell_list:
        if(index < len(value_list)):
            cell.value = value_list[index]
            index += 1

    for i in cell_list:
        print(i)

    wks.update_cells(cell_list)
