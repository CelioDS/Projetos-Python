course = " PytHON 2          "

print(f"""
{course.upper()}
{course.lower()}
{course.title()}
{course.strip()}.  #remove all spaces
{course.lstrip()}. #remove leading spaces
{course.rstrip()}. #remove trailing spaces
{course.join('-')}
{course.center(10,"#")}
{"-".join(course.strip())}
""")

menu = "PYTHON"
print(menu.center(20, " "))

name = "Célio da silva santos"


print(name[0])
print(name[:5])
print(name[5:])
print(name[0:10])
print(name[0:10:2])
print(name[:])
print(name[:: -1])


message = f"""
hi, my name is {name},
 i am learning python
"""

print(message)

print("""

===menu===

1 - deposito
2 - sacaar
3 - sair

""")