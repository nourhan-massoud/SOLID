# A class should have ONE responsibility and no more .
# like in this example we have two class
# first one to collect all books on on dic
# second one to store all books as strings in file will be create it also
# if we make frist one store books in file , this behavior break single responsibility princple .
# https://www.youtube.com/watch?v=NwiKVKj4uX8&list=PLUZKbOMoLPXDfscOjz87IJmsCvfXG0u5K&index=1


class Books():
    def __init__(self):
        self.books = {}
        self.number = 0

    def add_book(self,book):
        self.number += 1
        self.books[self.number] = book

    def __str__(self):
        return str(self.books)
    
    # store_books method now break single responsibility 
    # if we need not break single responsibility we should create new class
    # which that make do another task 

    # def store_books(self,filename):
    #     with open (filename , 'w') as file:
    #         file.write(str(self.books))

class StoreBooks():
    @staticmethod
    def store_books(filename,books):
        
        with open (filename , 'w') as file:
            file.write(str(books))


items = Books()   
items.add_book("Book A")   
items.add_book("Book B")  
items.add_book("Book C")    

print(f"The books i have to read are :{items}")
# items.store_books("test_file.txt")

store = StoreBooks()
store.store_books("test_file.txt",items)  

