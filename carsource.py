import Classes as c

from Classes import Car, Company

def print_menu():
    print("1. Add car")
    print("2. Show car list")
    print("2. Show car data")
    print("3. Delete car")
    print("4. Exit")
    
myCompany = c.Company("Up Cars")
program_running = True



while program_running:
    print_menu()
    option = int(input("Enter option: "))
    match option:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            program_running = False
        case _: 
            print("Invalid option")
    