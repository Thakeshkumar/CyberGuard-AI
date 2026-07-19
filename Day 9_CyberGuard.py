# Day - 9
# Topic : CyberDuard
# Project : CyberGuard AI

print("=======================================")
print("          CyberGuard AI           ")
print("=======================================")

# Function to analyze password strength

def password_analyzer(password):
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
        print("password strength : MEDIUM")

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

# Function to scan URL and check its validity and domain reputation
def url_scanner():
     
     url = input("Enter the URL to scan: ")
     # Placeholder for URL scanning logic

     if url.startswith("http://") or url.startswith("https://"):
          print("The URL is valid.")
     else:
          print("The URL is invalid. Please enter a valid URL starting with http:// or https://")

     # check domain reputation (placeholder logic)
     
     if ".com" in url:
          print("🌍 Commercial Website (.com) Generally Safe" )

     elif ".org" in url:
          print("🏢 Organization Website (.org) Generally Safe" )

     elif ".net" in url:
          print("🌐 Network Website (.net) Generally Safe")

     else:
          print("Unknown Domain")

     input("\n  Press Enter To Return To Main Menu ...")


def scam_detector():
     print("\n Scam Detector is under development. Please check back later for updates.")

# menu for the user to select the desired functionality
while True:
    print("\nSelect an option:")
    print("1. Password Analyzer")
    print("2. URL Scanner")
    print("3. Scam Detector")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        password = input("Enter Your Password :")
        password_analyzer(password)
    elif choice == '2':
        url_scanner()
    elif choice == '3':
        scam_detector()
    elif choice == '4':
        print("Thank you for using CyberGuard AI. Goodbye!")
        print("=======================================")
        break
    else:
        print("Invalid choice. Please try again.")




