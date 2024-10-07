#Словари
my_dict = {'Nikita': 1982, 'Anton' : 1991, 'Ildar' : 1987}
print(my_dict)
print(my_dict['Nikita'])
my_dict['Kamila'] = 2012
my_dict['Edik'] = 1990
del my_dict['Anton']
print(my_dict)
# Множества
my_set = {1, 2, 3, 4, 10, 2, 1, 2, True, 'Anton'}
print(my_set)
my_set = {1, 2, 3, 4, 10, 2, 1, 2, True, 'Anton', 'Nikita', 'Robert'}
print(my_set.remove(2))
print(my_set)