# for loop iterating over a range object and a list object

# calls a range object
for i in range(3):
    print(i) 

# calls a list object
for i in ['c', 'a', 't']:
    print(i)

# when used in a for loop, Python calls the built in iter() and next() functions
# when used in a for loop, iterable objects are passed to the iter() func 
# and returns iterator objects

# entering iter() and next() funcs manually

iterable_obj = range(3)
print(iterable_obj)

iterator_obj = iter(iterable_obj)
i = next(iterator_obj)
print(i)


i = next(iterator_obj)
# print(i)


i = next(iterator_obj)
# print(i)

# i = next(iterator_obj)
# print(i)

iterable = list('cat')
print(iterable)

final_str = []
for i in range(12):
    final_str.append('hi')
final_str = ' '.join(final_str)
print(final_str)

letters = ['a', 'Z', 'b', 'Y']
letters.sort(key=str.lower)
print(letters)