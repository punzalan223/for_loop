group = int(input("Enter a number of members in a group: "))
age_price = []
numbers_group = []

for i in range(group):
    age = int(input("Enter Guest Age (Black to End) : "))
    if age<=2:
        price = 00.00
        numbers_group.append(age)
        age_price.append(price)
    elif age>=3 and age<=12:
        price = 50.00
        numbers_group.append(age)
        age_price.append(price)
    elif age>=65:
        price = 60.00
        numbers_group.append(age)
        age_price.append(price)
    else:
        price = 80.00
        numbers_group.append(age)
        age_price.append(price)

print("+-------+-------------+---------+")
print("|--No.--+--Guest Age--+--Price--|")
print("+-------+-------------+---------+")
group_length = len(numbers_group)
for i in range(group_length):
    print(f"| {i+1:^5} | {numbers_group[i]:^4}yrs old | P{age_price[i]:^6.2f} |")
print("+-------+-------------+---------+")
print("The Total Cost is: ",end="")
print(sum(age_price))
