# day_4 menu 
# project ("CyberGuard AI")
# Developer : Thakesh kumar

print("=================================")
print("     CyberGuard AI   ")
print("=================================")

print("1: URL scanner ")
print("2: Password Analyzer ")
print("3: Scam Analyzer ")
print("4: Exit")

username = input("Enter your Name :")
# choose opeartion for compare
choose = int(input("\n choose Option ")) 

if choose == 1:
    print(" URL Scanner Opening...",username)

elif choose == 2:
    print("Password Analyzer Opening...",username)

elif choose == 3:
    print(" Scam detector Opening...",username)

elif choose == 4:
    print("ThankYou For Using CyberGuard AI ")

else:
    print("Invalid option !!")
    


