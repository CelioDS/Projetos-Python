
print(set([1,2,3,4,5,5,3,2])) #set removes duplicate

print(set("pineapple"))
print(set(["pineapple", 'box', 'jackfruit','apple', "apple", 'Apple']))

set_a = {1,3,2}
set_b = {2,4,5}


print(set_a.union(set_b))
print(set_a.intersection(set_b)) # equal
print(set_a.difference(set_b)) # different
print(set_b.difference(set_a)) # different
print(set_b.symmetric_difference(set_a)) # different

print(set_a.issubset(set_b)) #

print(set_b.issubset(set_a)) #
print(set_b.issubset(set_a)) #

print(set_b.isdisjoint(set_a)) #

set_b.add(8)
set_b.add(7)
set_b.add(0)
set_b.discard(2)
set_b.pop() #{5, 7, 8}



print(set_b)



