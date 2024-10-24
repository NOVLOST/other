import xlsxwriter as xl
from bars import card_maker
def excel(data):
    book = xl.Workbook(r"C:\Users\SYXAЧ\Desktop\флэшка\custom.xlsx")
    page = book.add_worksheet("товар")

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    for i in data():
        page.write(row , column, i[0])
        page.write(row, column + 1, i[1])
        page.write(row, column + 2,  i[2])
        page.write(row, column + 3, i[3])
        row += 1
    book.close()

excel(card_maker)
