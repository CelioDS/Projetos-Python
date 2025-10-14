

def newPassword(a, b):
    arrayA = list(a)
    arrayB = list(b)

    print(arrayB)

    new_pass = []
    # Write your code here
    for i in range(len(arrayA)):
        new_pass.append(arrayA[i])
        new_pass.append(arrayB[i])


    new = "".join(new_pass)
    print(new)
    return new_pass


a = 'abc'
b = 'dfg'

newPassword(a,b)
