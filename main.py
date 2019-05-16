import other_functions
import user_functions

close = False
while not close:
    print("\n----------------------------------------------------"
          "\nEnter the corresponding number to use the functions: "
          "\n1. Book Searcher"
          "\n2. All Book list"
          "\n3. Rent Book"
          "\n4. Rented book info"
          "\n5. Get Books Back"
          "\n0. to end program")

    user_input = int(input(">"))
    if user_input == 1:
        other_functions.book_searcher()
    elif user_input == 2:
        other_functions.book_avilable()
    elif user_input == 3:
        user_functions.book_borrow()
    elif user_input == 4:
        other_functions.borrow_info_reader()
    elif user_input == 5:
        user_functions.return_book()
    elif user_input == 0:
        print("Closing program...")
        close = True
    else:
        print("Input Invalid")


