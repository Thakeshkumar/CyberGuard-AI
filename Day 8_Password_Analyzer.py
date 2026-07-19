# Day 8
# Topic: password Analyzer
# Project : CyberGuard AI

print("========================================")
print("     CyberGuard AI       ")
print("========================================")

password = input("Enter Your Password :")

upper=0
lower=0
number=0
special=0

for letter in password:

    if letter.isupper():
        upper = upper + 1

    if letter.islower():
        lower = lower + 1

    if letter.isdigit():
        number = number + 1

    if letter in "@#$%^&*":
        special = special + 1

print("Password length :",len(password))
print("Uppercase :",upper)
print("Lowercase :",lower)
print("Number :",number)
print("Special Character :",special)

# password strength check

if len(password) >= 8 and upper > 0 and lower > 0 and number > 0 and special >0:
    print("password strength : STRONG")

elif len(password) >= 8:
    print("password strength : MENDIUM")

else:
    print("password strength : WEAK")

if upper == 0:
        print("Add atleast 1 uppercase letter")

if lower == 0:
        print("Add atleast 1 lowercase letter")

if number == 0:
        print("Add atleast 1 number")

if special == 0:
        print("Add atleast 1 special character")

print("     Thanking for using CYBERGUARD AI ")

print("========================================")

