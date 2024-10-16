import os
import platform
import time

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

value_1 = 10
value_2 = 5
limit = 8

for i in range(limit):
    if i == 0:
        print(f"addition {value_1 + value_2}")
    if i == 1:
      print(f"subtraction {value_1 - value_2}")
    if i == 2:
         print(f"multiplication {value_1 * value_2}")
    if i == 3:
         print(f"division {value_1 / value_2}")
    if i == 4:
        print(f"division integer {value_1 // value_2}")
    if i == 5:
        print(f"exponential {value_1 ** value_2}")
    if i == 6:
        print(f"modulo {value_1 % value_2}")

print(f"\nOrder of precedence {value_1 + (value_1 / value_2)}\n")

time.sleep(3)
os.system("cls")
balance_1 = 4000
balance_2 = 4000
limit_balance = 6

for i in range(limit_balance):
    
    if i == 0:
        print(f"equal {balance_1 == balance_2}")
    if i == 1:
        print(f"different {balance_1 != balance_2}")
    if i == 2:
        print(f"greater {balance_1 > balance_2}")
    if i == 3:
        print(f"greater equal {balance_1 >= balance_2}")
    if i == 4:
        print(f"less {balance_1 < balance_2}")
    if i == 5:
        print(f"less equal {balance_1 <= balance_2}")
 

clear_screen()



