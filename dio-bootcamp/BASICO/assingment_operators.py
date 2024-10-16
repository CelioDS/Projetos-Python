balance_1 = 2

obj_assignment_operators= [
   ("sum", lambda x: x + 2),
   ("less", lambda x: x - 2),
   ("multiply", lambda x: x * 2),
   ("division", lambda x: x / 2),
   ("exponential", lambda x: x ** 2),
   ("integer division", lambda x: x // 2),
]

for description, operators  in obj_assignment_operators:
    balance_1 = operators(balance_1)
    print(balance_1)

