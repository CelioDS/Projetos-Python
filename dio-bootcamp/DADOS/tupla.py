fruit = ("orange", 'cramp',)


number =  tuple([0,1, 2, 3, 4, 5, 6])
print(number[0])


number = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(number[0])      # [1, 2, 3]
print(number[0][2])   # [3]
print(number[-1][-1]) # [9]


tupleNwe = ['c','e','l','i','o'] #imutavel

print(tupleNwe[2:])
print(tupleNwe[0:2:1])
print(tupleNwe[::])
print(tupleNwe[::-1]) #REVERSE


car = ("gol")
car_tuple = ("gol",)
print(isinstance(car, tuple))
print(isinstance(car_tuple, tuple))