# This is O(1), constant time because regardless of how 
# long the data is, the function performs one task and returns it
# in the same exact amount of time because it is doing one operation only 

def get_first_element(lst):
    if len(lst) > 0:
        return lst[0]
    else:
        return None

my_lst = [1, 2, 3, 4, 5]
result = get_first_element(my_lst)
print(result)

arr = [1 , 2, 3, 4, 5]
print(len(arr))

# O(log n) Logarithmic
# Splits data in half, searches one half, if target is below or above half, 
# splits data in half again to search for target. Data can double, triple, quadruple etc.
# but algorithm performance/runtime time only increases by one step


def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        
        
# Returns the index of the `target` parameter    
print(binary_search([1, 2, 3, 4, 5, 6,], 4))