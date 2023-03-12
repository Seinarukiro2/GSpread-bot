import gspread

file = 'credentials.json' 

# connection to credential account 
gs = gspread.service_account(file)

#connection to sheets file
my_doc = gs.open('+ и -')

# selecting a worksheet
work_sheet = my_doc.worksheet('+ и -')

async def get_document_link():
    return my_doc.url


async def get_total():
    result = sum(list(map(int, work_sheet.col_values(1)[1:]))) - sum(list(map(int, work_sheet.col_values(3)[1:])))
    return result


async def add_new_earnings(value):
    work_sheet.update_cell(len(work_sheet.col_values(1)) + 1, 1, value)


async def add_new_expenditure(value):
    work_sheet.update_cell(len(work_sheet.col_values(3)) + 1, 3, value)

