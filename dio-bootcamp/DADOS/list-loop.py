test_list = ['orange', 'apple', 'grape',{'curso':'python'}]

test_list.sort(reverse=True)


copy_list = test_list.copy()
copy_list.clear()
print(copy_list,'list copy'
                '')
for item, index in enumerate(test_list):
    print(index, item, end=" - ")

number = list(range(10))
even = []

for num in number:
    if num % 2 == 0:
        even.append(num)
print(even)

test_list.append(41)
test_list.append('tetes')
test_list.append([40,23,56])
test_list.append({'nome': 'celio'})
test_list.extend(['new','data'])
print(test_list.index('data'))

test_list.pop() #last - data
test_list.pop(0) #first - orange
test_list.remove('new') #new

test_list.reverse()


for item in test_list:
    print( item, end=" - ")