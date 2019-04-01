largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        else:
            number = int(num)
    except ValueError:
        print("Invalid input")
        continue


    if largest is None :
        largest = number
        smallest = number

    elif number > largest:
        largest = number

    elif int(num) < smallest:
        smallest = number

print("Maximum is", largest)
print("Minimum is", smallest)