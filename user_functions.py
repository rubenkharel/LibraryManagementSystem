import datetime
import list_builder
import other_functions
from pathlib import Path

list_of_books = list_builder.in_list()
information_of_borrower = list_builder.borrow_info_in_list()
def book_borrow():
    """This function handles the borrowing system of the programme"""
    borrower = input("Enter the name of the borrower: ")
    phone_num = input("Enter the phone number of the borrower: ")
    borrowing = True
    count = 1
    while borrowing == True:
        book_ID = input("Enter the bookID of particular book the user want to borrow: ")
        if other_functions.book_id_validity(book_ID):
            book_name = other_functions.book_id_to_name(book_ID)
            date_time = str(datetime.datetime.today().strftime("%Y/%m/%d at %I:%M:%S"))
            borrow_info = [book_name, ",", borrower, ",", phone_num, ",", date_time]

            available = Path("Borrow_remarks.txt")
            modes = "w+"
            if available.is_file():
                modes = "a"
            with open("Borrow_remarks.txt", modes) as borrow_file:
                borrow_file.writelines(borrow_info)
                borrow_file.write("\n")
            book_data_updater(book_ID)
            price_of_book = other_functions.paying_price(book_ID)
            print("Price of book: ", price_of_book, "\nFine amount after 10 days: 1$/day")
            check = True
            while check:
                print("Borrow next book?(y/n): ")
                again = str(input(">"))
                yes = "y"
                no = "n"
                if again.lower() == yes:
                    count = count + 1
                    if count > 2:
                        print("Sorry same user cannot checkout more then 2 books at a time.")
                        check = False
                        borrowing = False
                        break
                    break
                elif again.lower() == no:
                    check = False
                    borrowing = False
                    break
        else:
            print("Book ID did not found. Please Enter a correct book ID.")
            borrowing = True
    if count == 1:
        other_functions.borrower_note(1,borrower)
    elif count == 2:
        other_functions.borrower_note(2,borrower)
    elif count == 3:
        other_functions.borrower_note(2,borrower)
    else:
        print("Error")


def book_data_updater(book_ID):
    """This function updates the books.txt as soon as a book is borrowed."""
    row = 0
    max_row = len(list_of_books)
    while row < max_row:
        if book_ID == list_of_books[row][0]:
            current_quantity = int(list_of_books[row][3])
            current_quantity = current_quantity - 1
            inserting_value = str(current_quantity)
            list_of_books[row][3] = inserting_value
            break
        else:
            row = row + 1

    with open("books.txt", "w+") as overwrite:
        for row_index in list_of_books:
            for items in row_index:
                overwrite.write(items)
                if not row_index.index(items) == 4:
                    overwrite.write(",")
            overwrite.write("\n")


def return_book():
    """This function is used when a book is returned back to the library"""
    returning = True
    while returning == True:
        book_ID = input("Enter the book ID: ").lower()
        borrower_name = input("Enter the name of the borrower: ").lower()
        book_name = other_functions.book_id_to_name(book_ID)
        if other_functions.return_book_validity_checker(book_name, borrower_name):
            days_took = other_functions.date_calcualtor(borrower_name, book_ID)
            price_of_book = other_functions.paying_price(book_ID)
            fine_amount = 0
            total_amt = 0
            if days_took > 10:
                cut_days = days_took - 10
                fine_amount = cut_days * 1
                total_amt = fine_amount + price_of_book
                print("The total amount to be paid is: "
                      "\n   Fine amount : ", fine_amount,
                      "\n+  Book Borrow Price : ", price_of_book,
                      "\n-----------------------"
                      "\n   Total amount: ", total_amt)
            else:
                total_amt = price_of_book
                fine_amount = 0
                print("The total amount to be paid is: "
                      "\n   Fine amount : ", fine_amount,
                      "\n+  Book Borrow Price : ", price_of_book,
                      "\n------------------------"
                      "\n   Total amount : ", total_amt)

            time_returned = str(datetime.datetime.today().strftime("%Y/%m/%d at %I:%M:%S"))
            fine_for_list = str(fine_amount)
            total_amt_for_list = str(total_amt)
            return_info_list = [other_functions.book_id_to_name(book_ID), ",", borrower_name, ",", time_returned, ","
                , fine_for_list, ",", total_amt_for_list]
            available = Path("Return_book.txt")
            modes = "w+"
            if available.is_file():
                modes = "a"
            with open("Return_book.txt", modes) as return_info:
                return_info.writelines(return_info_list)
                return_info.write("\n")
            book_data_update_after_return(book_ID)
            check = True
            while check == True:
                search_again = str(input("\nReturn next book?(y/n): "))
                if search_again.lower() == "y":
                    check = False
                elif search_again.lower() == "n":
                    check = False
                    returning = False
                    break
                else:
                    print("Invalid Input")
        else:
            print("Book and Borrower name did not match.")
            returning = True

def book_data_update_after_return(book_ID):
    list_books = list_builder.in_list()
    information_borrower = list_builder.borrow_info_in_list()

    row = 0
    max_row = len(list_books)
    while row < max_row:
        if other_functions.book_id_to_name(book_ID) == list_books[row][1]:
            current_quantity = int(list_books[row][3])
            current_quantity = current_quantity + 1
            inserting_value = str(current_quantity)
            list_books[row][3] = inserting_value
            break
        else:
            row = row + 1

    with open("books.txt", "w+") as overwrite:
        for row_index in list_books:
            for items in row_index:
                overwrite.write(items)
                if not row_index.index(items) == 4:
                    overwrite.write(",")
            overwrite.write("\n")

    book_name = other_functions.book_id_to_name(book_ID)
    max_row_x = len(information_borrower)
    row_x = 0
    while row_x < max_row_x:
        if book_name.lower() == information_borrower[row_x][0].lower():
            information_borrower.pop(row_x)
            break
        else:
            row_x = row_x + 1

    with open("Borrow_remarks.txt", "w+") as overwrite_x:
        for row_index_x in information_borrower:
            for item_x in row_index_x:
                overwrite_x.write(item_x)
                if not row_index_x.index(item_x) == 3:
                    overwrite_x.write(",")
            overwrite_x.write("\n")

