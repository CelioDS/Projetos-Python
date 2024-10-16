test_list = ['orange', 'grape','curso','python']
test_list.extend(['new','data'])
test_list.append({'nome':'celio'})

for index, item in enumerate(test_list):

    if index < len(test_list)-1:
        print( item, end=" - ")
    else:
        print()


test_list.remove({'nome':'celio'})
test_list.sort()
print(test_list)
test_list.reverse()
print(test_list)

test_list.sort(reverse=True)
print(test_list)

test_list.sort(key=lambda  x: len(x))
print(test_list)

test_list.sort(key=lambda  x: len(x), reverse=True)
print(test_list)


