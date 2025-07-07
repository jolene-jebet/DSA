numbers = [11,22,33,44,55,66,77,88,99]

key_value = 88
found = False
counter = 1

for num in numbers:
    if num == key_value:
        found = True
        print("Found at Position: ", counter)
        break

    counter += 1

if not found:
    print("Item not found")