found = 0  # this is used to confirm the output
i = 0  # this i is use for finding the position of the searched number

x = input("Number to search : ")  # taking input to search

xx = float(x)  # have to convert into integer or float because it was in string format, you can check the type of the input using  print(type(x))

# creating the list
list1 = [10, 55, 23, 69, 48.32, 100, 80, 110.90]

for j in list1:
    if j == xx: # in the first iteration, j = 10, so if 10 == searched number, then found else not found, and so on
        found = 1
        break
    else:
        found = 0
    i = i + 1

#ind = ar.index(xx)  #you can also find the position of the searched number using index, but i use 'i' instade of index, just to keep it simple

if found == 1:
    # print("Found",thing,"at location :", ind) # if you use index (line 19) then only, remove the line 24 and use this line

    print("Found", j, "at location :", i)

elif found == 0:
    print("\nError!! \nNumber not found!")
