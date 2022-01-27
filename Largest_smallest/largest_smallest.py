#Repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print the largest and smallest of the numbers, for invalid entry use try/except

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break       # loop break when num == done
    try:
        n = int(num)  # change the value to integer or float otherwise it will give error
    except:
        print("Invalid input")
        continue     # otherwise, it will go to the next instead of going back to top

    if largest is None or n > largest:
        largest = n
    elif smallest is None or n < smallest:
        smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)
