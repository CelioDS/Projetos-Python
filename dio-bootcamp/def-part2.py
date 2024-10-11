#def f (pos1, pos2, /, pos or kwd, * , kwd1, kwd2)
#    position only     position ou keyword       keyword only

def create_car(model,year, plate_license,/,brand, engine, fuel):
    print(model,year,plate_license,brand,engine,fuel)

create_car('bmw 3', 2024, 'xtc122', 'bmw','1.0','alcohol')
create_car('bmw 2', 2024, 'xtc1622', brand='bmw',engine='1.9',fuel='gasoline')


def create_car2(model,year, plate_license,/,*,brand, engine, fuel):
    print(model, year, plate_license, brand, engine, fuel)

create_car2('bmw 2', 2024, 'xtc1622', brand='bmw',engine='1.9',fuel='diesel')


def sum_add(a,b):
    return a + b
def subtract_add(a,b):
    return a - b

def show_result(a,b,function_sum):
    result = function_sum(a,b)
    print(f"\nthe result is {a}+{b}={result}")

show_result(10,5,sum_add)
show_result(10,5,subtract_add)

