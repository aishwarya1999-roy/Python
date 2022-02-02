# Search element in a list using boolean variable

#True and False are boolean variable

found = False  # this is act as flag variable 
i = 0  # this i is use for finding the position of the searched number

x = input("Number to search : ")  # taking input to search

xx = float(x)  # have to convert into integer or float because it was in string format, you can check the type of the input using  print(type(x))

# creating the list
list1 = [10, 55, 23, 69, 48.32, 100, 80, 110.90]

for j in list1:
    if j == xx: # in the first iteration, j = 10, so if 10 == searched number, then found else not found, and so on
        found = True
        break
    else:
        found = False
    i = i + 1

#ind = list1.index(xx)  #you can also find the position of the searched number using index, but i use 'i' instade of index, just to keep it simple

if found == True:
    # print("Found",j,"at location :", ind) # if you use index (line 23) then only, remove the line 28 and use this line

    print("Found", j, "at location :", i)

elif found == False:
    print("\nError!! \nNumber not found!")
