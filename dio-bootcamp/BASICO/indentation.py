import time

balance = 100

def sake(sake_value: float):
    global balance
    print(f"Sake {sake_value} loading....")
    time.sleep(2)

    if sake_value <= balance:
        balance -= sake_value
        print(f"withdrawal completed {sake_value} remaining {balance}")
        print('__________________')
    else:
        print(f"insufficient balance,your balance {balance}.")
        print('__________________')

def deposit(deposit_value: float):
    global balance
    print(f"deposit  loading....")
    time.sleep(2)

    balance += deposit_value
    print(f"your balance is {balance}")
    print('__________________')


sake(150)
time.sleep(2)
deposit(100)
time.sleep(2)
sake(100)