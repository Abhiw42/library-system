
def books():
     print("Press 1 for 101 Book Info ")
     print("Press 2 for 102 Book Info ")
     print("Press 3 for 103 Book Info ")
     print("Press 4 for 104 Book Info ")
     print("Press 5 for 105 Book Info ")
     a=int(input(""))
     if (a==1):
          print("Title        : Python ")
          print("Author       : Guido Van Rossum ")
          print("Price        : Rs 300 ")
          print("Launch date  : 12/12/2000 ")
          print("No. of pages : 298")
          print("")
          def invalid():
               b=int(input("Press 1 for main menu and press 2 to exit : "))
               if(b==1):
                  books()
               elif(b==2):
                  print("Thanku for visiting Skill circle library system")
               else:
                  print("Invalid input")
                  invalid()
          invalid()
     elif (a==2):
          print("Title        : C ")
          print("Author       : Dennis Ritchie ")
          print("Price        : Rs 340 ")
          print("Launch date  : 12/12/2001 ")
          print("No. of pages : 290")
          print("")
          def invalid():
               b=int(input("Press 1 for main menu and press 2 to exit : "))
               if(b==1):
                  books()
               elif(b==2):
                  print("Thanku for visiting Skill circle library system")
               else:
                  print("Invalid input")
                  invalid()
          invalid()
     elif (a==3):
          print("Title        : Java ")
          print("Author       : James Gosing ")
          print("Price        : Rs 340 ")
          print("Launch date  : 10/12/1990 ")
          print("No. of pages : 190")
          print("")
          def invalid():
               b=int(input("Press 1 for main menu and press 2 to exit : "))
               if(b==1):
                  books()
               elif(b==2):
                  print("Thanku for visiting Skill circle library system")
               else:
                  print("Invalid input")
                  invalid()
          invalid()
     elif (a==5):
          print("Title        : C++ ")
          print("Author       : Bjarne Stroustrup ")
          print("Price        : Rs 400 ")
          print("Launch date  : 12/08/2015 ")
          print("No. of pages : 690")
          print("")
          def invalid():
               b=int(input("Press 1 for main menu and press 2 to exit : "))
               if(b==1):
                  books()
               elif(b==2):
                  print("Thanku for visiting Skill circle library system")
               else:
                  print("Invalid input")
                  invalid()
          invalid()
     elif (a==5):
          print("Title        : C# ")
          print("Author       : Peter Golde ")
          print("Price        : Rs 340 ")
          print("Launch date  : 03/09/1990 ")
          print("No. of pages : 290")
          print("")
          def invalid():
               b=int(input("Press 1 for main menu and press 2 to exit : "))
               if(b==1):
                  books()
               elif(b==2):
                  print("Thanku for visiting Skill circle library system")
               else:
                  print("Invalid input")
                  invalid()
          invalid()
     else:
          print("invalid input")
          books()
     

books()
        