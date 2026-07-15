# Day 7
# Topic : while loop _ Menu
# project : CyberGuard AI

print("=======================================")
print("     CyberGuard AI       ")
print("=======================================")

while True:
    print("\n 1. URL Scanner ")
    print(" 2. Password Analyzer")
    print(" 3. Scam Detector")
    print(" 4. Exit")

    choice = int(input(" \n Choose option :"))

    if choice == 1:
        print(" Opening URL Scanning...")

    elif choice == 2:
        print(" Opening Password Analyzer...")

    elif choice == 3:
        print(" Opening SCAM Detector...")

    elif choice == 4:
        print(" Thanking For Using CyberGuard AI ")
        break

    else:
        print(" Invalid Option !!")
 