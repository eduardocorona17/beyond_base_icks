import copy

# Unpythonic
animals = ['cat', 'dog', 'horse']
for i in range(len(animals)):
    print(i, animals[i])

# Pythonic
other_animals = ['Deer', 'Lion', 'Whale']
for i, animal in enumerate(other_animals):
    print(f"\n{i, animal}")  # This prints as a Tuple.

other_animals = ['Jackelope', 'Lion', 'Whale']
for i, animal in enumerate(other_animals):
    print(i, animal) # Prints out normally. How do I get it to print on a new line?

spizzle = 42

print(f'This prints the value in spizzle: {spizzle}.')

print(f'This prints literal curly braces: {{spizzle}}')
print('Hello, world!'[7:12])
print('Hello, world!'[:5])
print(['cat', 'dog', 'mouse', 'eel'][2:])

spam = ['cat', 'dog', 'mouse', 'eel']
eggs = spam[:]
print(spam)
print(eggs)
print(id(spam) == id(eggs))

# copy() creates shallow copies just as '[:]' does.
eggs = copy.copy(spam)
print(f"\n{eggs}")

number_of_pets = {'dogs': 2, 'cats': 1}
print('I have', number_of_pets.get('cats', 0), 'number of cats') # returns value of key in get() 1 in this case.

# Unpythonic example
num_of_pets = {'dogs': 3}
if 'cats' not in num_of_pets:
    num_of_pets['cats'] = 0

num_of_pets['cats'] += 10
print(num_of_pets['cats'])

# Pythonic Example
num_of_pets = {'dogs': 2}
num_of_pets.setdefault('cats', 0) # Does nothing if 'cats' exist

num_of_pets['cats'] += 22
print(num_of_pets['cats'])

holiday = {
    'Winter': 'New Year\'s Day',
    'Spring': 'May Day',
    'Summer': 'Juneteenth',
    'Fall': 'Halloween'}.get('season', 'Personal day off')
print(holiday)

# Ternary

value_if_True = 'Access granted'
value_if_False = 'Access denied'

condition = True

message = value_if_True if condition else value_if_False
print(message)

condition = False

message = value_if_True if condition else value_if_False
print(message)

age = 30

age_range = 'child' if age < 13 else 'teenager' if age >= 13 and age < 18 else 'adult'
print(age_range)