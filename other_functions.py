import list_builder
import datetime
import random

list_of_books = list_builder.in_list()
information_of_borrower = list_builder.borrow_info_in_list()

def book_searcher():
    """This function search the book searched by the user"""
    searching = True
    while searching == True:
        book_name = []
        query = input("Enter the name of the book you want to search: ")
        book_name.append(query)
        row = 0
        max_index = len(list_of_books)
        found = False
        while row < max_index:
            if book_name[0].lower() == list_of_books[row][1].lower():
                found = True
                print("We have the book you are searching for.")
                print("Book ID: ", list_of_books[row][0],
                      "\nBook Name: ", list_of_books[row][1],
                      "\nWriter: ", list_of_books[row][2],
                      "\nBook quantity available: ", list_of_books[row][3],
                      "\nBook Price: ", list_of_books[row][4])
                break
            else:
                row = row + 1
        if not found:
            print("Sorry, the book you are searching for is not available.")
        check = True
        while check == True:
            search_again = str(input("\nSearch again?(y/n): "))
            if search_again.lower() == "y":
                check = False
            elif search_again.lower() == "n":
                check = False
                searching = False
                break
            else:
                print("Invalid Input")


def book_avilable():
    """Prints all the book found in the library"""
    print("Below are the books we have in our library: ")
    row = 0
    book = 1
    id = 0
    max_row = len(list_of_books)
    print("Book ID\t\t\t\tBook Name")
    while row < max_row:
            book_name = list_of_books[row][book]
            book_id = list_of_books[row][id]
            print(book_id,"\t\t\t\t",book_name)
            row = row + 1


def book_id_to_name(book_ID):
    row = 0
    max_row = len(list_of_books)
    book_name = ""
    while row < max_row:
        if book_ID.lower() == list_of_books[row][0].lower():
            book_name = (list_of_books[row][1])
            break
        else:
            row = row + 1
    return book_name

def paying_price(book_ID):
    """This function extract the price of book per ten days."""
    price_num = 0
    row = 0
    max_row = len(list_of_books)
    while row < max_row:
        if book_ID.lower() == list_of_books[row][0].lower():
            price = list_of_books[row][4]
            price_num = float(price.strip("$"))
            break
        else:
            row = row + 1
    return price_num

def date_calcualtor(borrower_name, book_ID):
    row = 0
    date_taken = ""
    max_row = len(information_of_borrower)
    while row < max_row:
        if borrower_name.lower() == information_of_borrower[row][1].lower() and book_id_to_name(book_ID).lower() == \
                information_of_borrower[row][0].lower():
            date_taken = information_of_borrower[row][3]
            break
        else:
            row = row + 1
    splitter = date_taken.split("at")
    date_taken_list = [splitter]
    date_format = "%Y/%m/%d"
    date_returned = datetime.datetime.today().strftime("%Y/%m/%d")
    dateT = datetime.datetime.strptime(date_taken_list[0][0].strip(" "), date_format)
    dateR = datetime.datetime.strptime(date_returned, date_format)
    delta = dateR - dateT
    delta_days = delta.days
    return delta_days

def borrow_info_reader():
    print("Below is the information of all the borrowers: ")
    for row in information_of_borrower:
        for info in row:
            if row.index(info) == 0:
                print("------------------------------")
                print("Book Name: ", info)
            elif row.index(info) == 1:
                print("Borrower Name: ", info)
            elif row.index(info) == 2:
                print("Borrower contact info: ", info)
            elif row.index(info) == 3:
                print("Book taken date: ", info)
            elif row.index(info) == 4:
                print("")


def return_book_validity_checker(book_name, borrower_name):
    max_row = len(information_of_borrower)
    row = 0
    valid = False
    while row < max_row:
        if information_of_borrower[row][0].lower() == book_name.lower() and\
                borrower_name.lower() == information_of_borrower[row][1].lower():
            valid = True
            break
        else:
            row = row + 1
            valid = False
    return valid

def book_id_to_price(book_id):
    row = 0
    max_row = len(list_of_books)
    price = ""
    while row < max_row:
        if book_id.lower() == list_of_books[row][0].lower():
            price = (list_of_books[row][4])
            break
        else:
            row = row + 1
    return price

def book_name_to_id(book_name):
    row = 0
    max_row = len(list_of_books)
    book_id = ""
    while row < max_row:
        if book_name.lower() == list_of_books[row][1].lower():
            book_id = (list_of_books[row][0])
            break
        else:
            row = row + 1
    return book_id


def borrower_note(count, borrower):
    invoice_num = random.randint(1,99999999999)
    if count == 2:
        borrower_info = list_builder.borrow_info_in_list()
        maximim = len(borrower_info)
        max_check = maximim - 1
        sec_last = maximim - 2
        borrower_name = borrower

        book_name1 = borrower_info[sec_last][0]
        book_name2 = borrower_info[max_check][0]

        book_id1 = book_name_to_id(book_name1)
        book_id2 = book_name_to_id(book_name2)

        book_price1 = book_id_to_price(book_id1)
        book_price2 = book_id_to_price(book_id2)

        book_price1_float = book_price1.strip("$")
        book_price2_float = book_price2.strip("$")

        total = float(book_price1_float) + float(book_price2_float)
        strt = str(total)

        date_time = str(datetime.datetime.today().strftime("%Y/%m/%d at %I:%M:%S"))

        with open("./Invoice/"+borrower_name+str(invoice_num)+".txt","w+") as bn:
            bn.write("*************************************\n")
            bn.write("Issued to: "+borrower_name+"\n")
            bn.write("Issued date: "+date_time+"\n")
            bn.write("-------------------------------------\n")
            bn.write("Books\t\t\tPrice\n")
            bn.write(book_name1+"\t\t\t"+book_price1+"\n")
            bn.write(book_name2+"\t\t\t"+book_price2+"\n")
            bn.write("Total: $"+strt+"\n")
            bn.write("*************************************")
        print("Note generated for 2 books")
    elif count == 1:
        borrower_info = list_builder.borrow_info_in_list()
        maximim = len(borrower_info)
        max = maximim - 1
        borrower_name = borrower
        book_name = borrower_info[max][0]
        book_id1 = book_name_to_id(book_name)
        book_price1 = book_id_to_price(book_id1)

        date_time = str(datetime.datetime.today().strftime("%Y/%m/%d at %I:%M:%S"))
        with open("./Invoice/"+borrower_name + str(invoice_num) + ".txt", "w+") as bn:
            bn.write("*************************************\n")
            bn.write("Issued to: " + borrower_name+"\n")
            bn.write("Issued date: " + date_time+"\n")
            bn.write("-------------------------------------\n")
            bn.write("Books\t\t\tPrice\n")
            bn.write(book_name + "\t\t\t" + book_price1+"\n")
            bn.write("Total: " + book_price1+"\n")
            bn.write("*************************************")
        print("Note generated for 1 book")
    else:
        print("Not able to generate Invoice. Error occurred")

def book_id_validity(book_id):
    max_row = len(list_of_books)
    row = 0
    valid = False
    while row < max_row:
        if list_of_books[row][0].lower() == book_id.lower():
            valid = True
            break
        else:
            row = row + 1
            valid = False
    return valid