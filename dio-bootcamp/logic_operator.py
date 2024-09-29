balance = 1000
sake = 110
limit = 150
special_account = True

print(balance >= sake)
print(limit >= sake)

print(f"and : {balance >= sake and sake <= limit}")
print(f"or  : {balance >= sake or sake <= limit}")
print(f"not : {not balance >= sake or sake <= limit}")
print(f"parenthesis : {(balance >= sake or sake <= limit) or (special_account and balance >= sake)}")

