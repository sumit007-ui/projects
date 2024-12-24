import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_']

print("Welcome to the PyPassword Generator!")

st_letters = int(input("How many letter would you like in your password ? \n"))
st_number = int(input(f"How many number would you like in your password ? \n"))
st_symbol = int(input(f"How many symbol would you like in your password ? \n"))

#easy level
# password = ""

# for i in range(0,st_letters+1):
#     password +=random.choice(letters)

# for i in range(0,st_number+1):
#     password +=random.choice(numbers)

# for i in range(0,st_symbol+1):
#     password +=random.choice(symbols)

# print(password)

#hard level

password_list = []

for i in range(0,st_letters+1):
    password_list.append(random.choice(letters))

for i in range(0,st_number+1):
    password_list.append(random.choice(numbers))

for i in range(0,st_symbol+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
print(password_list)

password = ""
for i in password_list:
    password += i

print(f"Your password is : {password}")
 
