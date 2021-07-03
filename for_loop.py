group = int(input("Enter the members of a group: "))
guest_age = []
guest_price = []
for x in range(group):
    age = int(input("Enter Guest Age (Blank to End) : "))
    if age <= 2:
        a = 0
        guest_age.append(age)
        guest_price.append(a)
    elif age >=3 and age<=12:
        a = 50
        guest_age.append(age)
        guest_price.append(a)
    elif age >=65:
        a = 60
        guest_age.append(age)
        guest_price.append(a)
    else:
        a = 80
        guest_age.append(age)
        guest_price.append(a)

print("+-----+-------------+--------+")
print("| No. |  Guest Age  | Price  |")
print("+-----+-------------+--------+")
my_list_length = len(guest_age)
for i in range(my_list_length):
    print("| {:^3} |{:^5}yrs old | ₱{:<5.2f} |".format(i,int(guest_age[i]),guest_price[i]))
print("+-----+-------------+--------+")
print("The Total cost is ₱",end="")
print(sum(guest_price))




