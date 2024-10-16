wage = 1500
list_1 = [1]

def sum_bonus(bonus,list_1):
    global wage
    list_aux = list_1.copy()
    list_aux.append(2)
    print(list_aux)
    return  wage + bonus

print(sum_bonus(500, list_1))
print(list_1)