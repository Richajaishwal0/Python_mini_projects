limit=0
class Library:
    def __init__(self):
        self.list1=["Mahabharata","Optimization Techniques","Physical Education"]
        print()
    def add(self):
        self.numm=int(input(("Enter the  numbers of book you want to add to the list of books in the library:")))
        for i in range (self.numm):
            inputt=input("Enter the name of book you want to add:\n")
            self.list1.append(inputt)
        print("Thank you for adding!!\n")
    def borrow(self):
       self.borr=int(input(("Enter the  numbers of book you want to borrow from the library(Maximum limit:3):")))
       if self.borr<=3:
           for i in range (self.borr):
                inputt=input("Enter the name of book you want to borrow:\n")
                a=self.list1.remove(inputt)
           print("Have a good day!!\n")
       else:
           print("Sorry , you have to reduce book count up to 3\n")
    def show(self):
        print("The available books in the library are:" )
        for i in self.list1:
            print(i+" ")
obj=Library()
while (limit!=4):
    a=int(input("==Welcome to our library==\n1.Add the books to the library\n2.Borrow the books from the library\n3.Show all the books \n4.Exit\n"))
    if (a==3):
       obj.show()
    elif a==1:
        obj.add()
    elif a==2:
        obj.borrow()
    
  
