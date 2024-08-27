num_array = [3, -18, -23, 43, -100, 67- 43]
num = len(num_array)
def minimum_value():
    counter = 1
    min_value = num_array[0]
    while counter < num:
        assum_min_value = num_array[counter]
        if assum_min_value < min_value:
            min_value = assum_min_value
        else:
            min_value = min_value
        counter += 1
    return min_value

print(minimum_value())
