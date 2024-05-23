# >>> userscore = input("Give me a score value:")
# Give me a score value:56
# >>> userscore
# '56'
# >>> userscore_in_int = int(userscore)
# >>> userscore_in_int
# 56
# >>> userscore_in_int / 2
# 28.0

age = input("Provide me age: ")
int_age = int(age)

# induntation me jo bhi code hoga usko if k andar k mana jayega
# agar nhi hua to uske bahar
if (int_age<13):
    print("Child")
elif int_age<20:
    print("Teenager")
elif int_age<59:
    print("Adult")
else:
    print("Senior")
