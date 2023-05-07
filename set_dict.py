spam = {str(number) for number in range(10) if number % 2 != 0}  # Set comprehension
print(spam)

spam_2 = {str(number): number for number in range(10) if number % 2 != 0}  # Dictionary comprehension
print(spam_2)