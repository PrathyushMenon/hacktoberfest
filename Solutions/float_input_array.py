numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print("Enter number at location", i)
    item =  input()
    # accept float number from user
    # item = float(input()
    # add it to the list
    numbers.append(float(item))

print("User List:", numbers)
