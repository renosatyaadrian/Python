number = set()
print(dir(number))

number.add(1)
number.add('a')
number.add('b')
number.pop()
number.add('1')
print(number)

number_else = {1,"a"}
print(number_else.intersection(number))
