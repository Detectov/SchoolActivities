import os 
os.system("cls")
print("What's your name?")
name = input()
print("How many Watts per hour do you have on your bill?")
energy_consumption = float(input())


if energy_consumption < 50:
        print(f"{name}, your total is $50")
elif energy_consumption <= 100:
        total = energy_consumption * 1.1
        print(f"{name},your total is ${total}")
elif energy_consumption > 100 and energy_consumption < 200:
        total = energy_consumption * 1.2
        print(f"{name}, your total is ${total}")
elif energy_consumption > 200 and energy_consumption < 300:
        total = energy_consumption * 1.3
        print(f"{name}, your total is ${total}")
elif energy_consumption > 300 and energy_consumption < 400:
        total = energy_consumption * 1.4
        print(f"{name},your total is ${total}")
elif energy_consumption > 400:
        total = energy_consumption * 1.5
        print(f"{name},your total is ${total}")

        
