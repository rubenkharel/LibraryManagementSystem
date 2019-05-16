def in_list():
    """Import data into list from text file"""
    stock = []
    with open("books.txt", "r") as Stock:
        fileRead = Stock.readlines()
        for line in fileRead:
            stock.append(line.strip("\n").split(","))
    return stock


def borrow_info_in_list():
    """Import data into list from text file"""
    info = []
    with open("borrow_remarks.txt", "r") as borrowers:
        borrow_read = borrowers.readlines()
        for line in borrow_read:
            info.append(line.strip("\n").split(","))
        return info
