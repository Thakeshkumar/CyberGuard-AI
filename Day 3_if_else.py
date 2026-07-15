print("============================================")
print("             CyberGuard AI V0.1      ")
print("============================================")

username = input("Enter your name :")


security_level = int(input("Enter your security level (1-10):"))

if security_level >= 8:
    print("Welcome:", username)
    print("security status : HIGH ACCESS")

elif security_level >=5 :
    print("Welcome:",username)
    print("Security status : MEDIUM ACCESS")

else: 
    print("Access Limited")
    print("Improve your security level :",username)
