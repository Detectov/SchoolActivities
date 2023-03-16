import os
os.system ("cls")

def oddlist(): 
    print ("Type a number: ")
    x = int(input())
    for i in range(x + 1): 
    
        if i % 2 != 0:
        
            print (i)


        
def comparelists():
    a = ['b', 'c', 'd', 'a', 'e', 'f', 'g', 'h']
    b = ['b','1','3','9','d','i', '10', 'g']
    print (f"a = {a} \nb = {b}")
    commonelem = 0
    for element in a: 
        if element in b:
            commonelem += 1
    print(f"{commonelem} common elements in the lists")



def replacelast():
    lsta = []
    lstb =[]
    print("Type the number of elements of the first list: ")
    a = int(input())
    for i in range (0, a):
        print("Type an element: ")
        elem1 = input()
        lsta.append(elem1)
    print (lsta)
    print ("Type the number of elements of the second list: ")
    b = int(input())
    for i in range (0, b):
        print("Type an element: ")
        elem2 = input()
        lstb.append(elem2)
    print (lstb)
    lsta[-1] = lstb
    print (f"{lsta}")



def movezeroestolast():
    a = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
    templist = []
    zeroes = []
    for i in range (len(a)):
        if a[i] !=0:
            templist.append(a[i])
        else:
            zeroes.append(a[i])
    print (f"{templist + zeroes}")



def unique_elem():
    x = []
    y = []
    z = []
    a = int(input("Type the number of elements of the first list: "))
    for i in range (0, a):
        elem1 = float(input("Type an element: "))
        x.append(elem1)
    b = int(input("Type the number of elements of the second list: "))
    for j in range (0, b):
        elem2 = float(input("Type an element: "))
        y.append(elem2)
    for element in x:
        if element not in y:
            z.append(element)
    for element in y:
        if element not in x:
            z.append(element)
    print(f"{z}")



def listintostring():
    a =[]
    string = ""
    x = int(input("Type the number of elements of the list: "))
    for i in range (0, x):
        elem1 = str(input("Type an element: "))
        a.append(elem1)
    for i in a:
        string += i
    
    print(string)



def avarage():
    a = []
    b = []
    print("Type the number of elements of the first list: ")
    x = int(input())
    for i in range (0, x):
        print("Type an element: ")
        elem1 = float(input())
        a.append(elem1)
    print ("Type the number of elements of the second list: ")
    y = int(input())
    for i in range (0,y):
        print("Type an element: ")
        elem2 = float(input())
        b.append(elem2)
    avg = sum(a+b) / len (a+b)
    print (f"{avg}")


    

    
def addProducts(products, stock, prices):
   a = int(input("Type the number of products that you want to add: "))
   for i in range(0, a):
       products.append(input("Type the name of the product: "))
       stock.append(int(input("Type the amount of the product in storage: ")))
       prices.append(float(input("Type the price of the product: ")))

       
    
def createsale(quantity, product, stock, price):
    s = str(input("What product did you sell?"))
    q = int(input("How many did you sell? "))
    stock[product.index(s)] - q
    quantity.append([s, q, price*q])



def viewsale(quantity):
    for products in quantity:
        print(f"Name: {products[0]} Quantity: {products[1]} Price: ${products[2][0]} Total: ${products[2][0]*products[1]}")
   




def sales():
    products, prices, stock, quantity = [], [], [], []
    
    print("What do you want to do?\n1. Add products\n2. See stock\n3. Create a sale\n4. View sales\n5. Exit")
    opt = int(input())
    while opt != 5:
        match opt:
            case 1:
                os.system("cls")
                addProducts(products, stock, prices)
            case 2:
                os.system("cls")
                for index, product in enumerate(products):
                    print(f"{index + 1}: {product} -> {stock[index]}")
            case 3:
                os.system("cls")
                createsale(quantity, products, stock, prices)
            case 4:
                os.system("cls")
                viewsale(quantity)
            case 5:
                os.system("cls")
                exit()
            case _:
                os.system("cls")
                print("Please enter a valid option")
        print("What do you want to do?\n1.Add products\n2. See stock\n3. Create a sale\n4. View sales\n5.Exit")
        opt = int(input())



print("What do you want to do?\n1. Make an odd number list\n2. Compare two lists\n3. Obtain a unique element from two lists\n4. Convert charcters into strings\n5. Replace the last element of a list\n6. Move the zeroes to the end of a list\n7. Calculate the avarage of two lists\n8. Sales\n9. Exit ")
option = int(input())
while option != 9:
    match option:
        case 1:
            os.system("cls")
            oddlist()
        case 2: 
            os.system("cls")
            comparelists()
        case 3:
            os.system("cls")
            unique_elem()
        case 4:
            os.system("cls")
            listintostring()
        case 5: 
            os.system("cls")
            replacelast()
        case 6:
            os.system("cls")
            movezeroestolast()
        case 7:
            os.system("cls")
            avarage()
        case 8:
            os.system("cls")
            sales()
        case 9: 
            os.system("cls")
            exit()
        case _:
            os.system("cls")
            print("Please enter a valid option")
    print("What do you want to do?\n1. Make an odd list\n2. Compare two lists\n3. Obtain a unique element from two lists\n4. Convert charcters into strings\n5. Replace the last element of a list\n6. Move the zeroes to the end of a list\n7. Calculate the avarage of two lists\n8. Sales\n9. Exit ")
    option = int(input())