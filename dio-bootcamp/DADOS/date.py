from datetime import date, datetime, timedelta
import random
import pytz

data = date.today()
method_date = ['today' ]
for i in method_date:
    method = getattr(date, i, None)

    if callable(method):
        print(f"{date.__name__}.{i}()")
        print(method())
    else:
        print("no method")

data_1 = date(2023,7,10)
print(data_1)
print( datetime(2023,7,8,4,23,55))
print("______________________________________________"*2)

letter = ["S","M","L"]

type_car = random.choice(letter)
time_S = 30
time_M = 45
time_L = 60

date_now = datetime.now()

if type_car == "S":
    estimated_date =  date_now + timedelta(minutes=time_S)
    print(f'the car {type_car} arrived at {date_now.strftime("%H:%M on %d/%m/%y")} and will be ready by {estimated_date.strftime("%H:%M on %d/%m/%y")}')

elif type_car == "M":
    estimated_date = date_now + timedelta(minutes=time_M)
    print(
        f'the car {type_car}  arrived at {date_now.strftime("%H:%M on %d/%m/%y")} and will be ready by {estimated_date.strftime("%H:%M on %d/%m/%y")}')

else:
    estimated_date = date_now + timedelta(minutes=time_L)
    print(f'the car {type_car} arrived at {date_now.strftime("%H:%M on %d/%m/%y")} and will be ready by {estimated_date.strftime("%H:%M on %d/%m/%y")}')


print(date.today() - timedelta(days=1))

time_set = datetime(2024, 10,19,18,18,15) - timedelta(hours=2)
print(f"{time_set.strftime("%H:%M")} and {time_set.time()}")


date_string = "20/07/2024 18:26"
date_string = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(date_string - timedelta(minutes=10))

print('*****'.center(75,'|'))

data = datetime.now(pytz.timezone('Europe/Oslo'))
print(data)
