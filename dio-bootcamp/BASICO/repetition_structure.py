text = 'celio'
vowels = "AEIOU"
for letter in text:
    if letter.upper() in vowels:
        print(letter, end="")

# range(stop) -> range object
# range(start, stop[, step]) ->  range object
# start = obligatory , start-step optional

print(list(range(4)))
for number in range(0,11):
    print(number, end=" ")

print("")
for number in range(5, 51, 5):
    print(number, end=" ")


option = 1

while True:
    try:
        option =  int(input('\n[1] again '
                            '\n[2] extract'
                            '\n[3] continue'
                            '\n[0] exit'
                            '\n'))
        if option == 1:
            print('sake....')
        elif option == 2:
            print("extract")
            continue
        elif option == 3:
            continue
            print("continue")
        elif option == 0:
            print("exit")
            break
        else:
            print("option invalid")
    except ValueError:
        print("Error, try again")
