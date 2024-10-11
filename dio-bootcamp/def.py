def  show_massage():
    print("ola mundo")

def  show_massage1(name):
    print(f"ola {name}")

def  show_massage2(name='anonimo'):
    print(f"ola {name}")

def  show_massage3(name):
    print(f"ola {name}")

show_massage()
show_massage1('celio')
show_massage2()
show_massage1(name='Ceçlio')



def calc_number_sum(number):
    return print(sum(number))

def return_num_prev_front(number):
    prev = number - 1
    front = number + 1

    return print(f"previous : {prev} {number} {front}")

calc_number_sum([1,5,6,3,8,9])
return_num_prev_front(10)


def return_none():
    print('sa')


print(return_none())