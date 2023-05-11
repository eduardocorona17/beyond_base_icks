comprehend = [str(n) for n in [5, 4, 3, 2, 1]]
print(comprehend)

comprehend = [n % 2 == 0 for n in [10, 9, 8, 7, 6, 5, 4]]
print(comprehend)

comprehend = [ n for n in [10, 9, 8, 7, 6, 5, 4] if n %2 == 0]
print(comprehend)

comprehend = [ n % 2 == 0 for n in [10, 9, 8, 7, 6, 5, 4] if n % 2 ==0]
print(comprehend)

comprehend = [n // 2 for n in [10, 9, 8, 7, 6, 5, 4] if n % 2 == 0]
print(comprehend)
comprehend = [n / 2 for n in [10, 9, 8, 7, 6, 5, 4]]
print(comprehend)