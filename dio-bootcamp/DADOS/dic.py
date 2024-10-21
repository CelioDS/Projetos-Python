person = {"name":"celio", "year":25}
person2 = dict(name='Celio', idade=25)
person["mobile"]=19989058345  
print(person)
print("-"*50)
dados_person = person.copy()

dados_person["name"] = 'Celio da silva'
dados_person["profession"] ="developer software"

contact = {
    'celio.01t@gmail.com' : person2,
    'celio.lk.cs@gmail.com' : person2
}
print(contact)
print("-"*50)

for person in contact:
    print(person, contact[person])
print("-"*50)

newPerson = dict.fromkeys(['name', 'mobile'], 'null')
newPerson['year'] = '18'
print(newPerson)
print("-"*50)

print(newPerson.get("years",{})) #get  key no error
print(newPerson.keys())
print(newPerson.items())
print(newPerson.values())
print("-"*50)

print(newPerson.pop("mobile", {})) # remove e get remove
newPerson.popitem() # remove
print("-"*50)

print(newPerson)
newPerson.setdefault('mobile', "19998058345") # add if only unique
print(newPerson)

print("-"*50)
newPerson.update({"name":"celio"})
print(newPerson)

print('name' in newPerson)
del newPerson['mobile']
print(newPerson)
print(newPerson.get('moto'))



