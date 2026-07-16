# Output the sum of a list's values
items: list = [10, 20, 30, 40, 50]

def sum_list(a_list_of_integers_goes_here):

    total: int = int(0)

    for item in a_list_of_integers_goes_here:
        total += item
    return total

result: int = int(sum_list(items))

print("Sum of elements in the list:", result)