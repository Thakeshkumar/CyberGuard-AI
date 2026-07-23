# Day - 9
# Topic : CyberDuard
# Project : CyberGuard AI

print("=======================================")
print("          CyberGuard AI           ")
print("=======================================")

# Function to analyze password strength

def password_analyzer(password):
    print("\n=============== PASSWORD ANALYZER REPORT ===============")
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

        print("Password must be atleast 8 characters long")
    


    if upper == 0:
            print("Add atleast 1 uppercase letter")

    if lower == 0:
            print("Add atleast 1 lowercase letter")

    if number == 0:
            print("Add atleast 1 number")

    if special == 0:
            print("Add atleast 1 special character")

# Function to scan URL and check its validity and domain reputation
def url_analyzer():
     
     score = 0
     
     url = input("Enter the URL to scan: ")
     print("\n=============== URL ANAYZER REPORT ===============")
     # Placeholder for URL scanning logic

     if url.startswith("http://") or url.startswith("https://"):
          print("The URL is valid.")
     else:
          print("The URL is invalid. Please enter a valid URL starting with http:// or https://")

     # check domain reputation (placeholder logic)
     
     if url.startswith("https://"):
        print("HTTPS          : SAFE")

     elif url.startswith("http://"):
        print("HTTPS        : NOT SECURE")
        score += 20

    # URL Length
     if len(url) > 50:
        print("URL Length     : SUSPICIOUS")
        score+= 20
     else:
        print("URL Length     : NORMAL")

    # @ Symbol
     if "@" in url:
        print("@ Symbol       : FOUND")
        score+= 25

    # IP Address Check
     if "://" in url:
            domain = url.split("://")[1].split("/")[0]
     else:
            domain = url.split("/")[0]

     parts = domain.split(".")

     ip = True

     if len(parts) == 4:
            for part in parts:
                if not part.isdigit():
                    ip = False
                break
     else:
            ip = False

     if ip:
      print("IP Address     : YES")
      score+= 20
     else:
       print("IP Address     : NO")

    # Suspicious Keywords
     keywords = ["login", "verify", "update", "bank", "secure", "account"]

     found = False

     for word in keywords:
        if word in url.lower():
            print("Keyword Found  :", word)
            score+= 15
            found = True

     if not found:
        print("Keyword Found  : None")

     print("\n==============================")
     print("\n Threat Score :", score, "/100")

     if score <= 20:
            print("Verdict      : LOW RISK")
     elif score <= 50:
            print("Verdict      : MEDIUM RISK")
     else:  
            print("Verdict      : HIGH RISK")
     
     if ".com" in url:
          print("🌍 Commercial Website (.com) Generally Safe" )

     elif ".org" in url:
          print("🏢 Organization Website (.org) Generally Safe" )

     elif ".net" in url:
          print("🌐 Network Website (.net) Generally Safe")

     else:
          print("Unknown Domain")

     input("\n  Press Enter To Return To Main Menu ...")

def email_analyzer():
      email = input("Enter the email address to analyze: ")
      print("\n=============== EMAIL ANALYZER REPORT ===============")
    
    # Check if the email address is valid
      if "@" not in email or "." not in email:
        print("Invalid email address ")
        return
      
    # Split the email address into username and domain  
      username,domain = email.split("@")
      print("Username:",username)
      print("Domain:",domain)

    #personal email decection
      personal_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
      if domain in personal_domains:   
        print("Email type: Personal Email")

      else:
        print("Email type: Business Email")


   
    #email format validation
      if domain.endswith(".com"):
           print("Commercial Domain")

      elif domain.endswith(".org"):
           print("Organization Domain")

      elif domain.endswith(".net"):
              print("Network Domain")

      elif domain.endswith(".edu"):
              print("Educational Domain")

      elif domain.endswith(".gov"):
              print("Government Domain")

      print("\n======================================")
      print("\n Basic Email Format looks valid")
    
    #Adding risk score based on email type
      score= 0

      if domain in personal_domains:
        score -= 50

      if len (username) < 3:
        score -= 20

      print("Security score:",score ,"/100")

      input("\n press enter to return to main menu ...")

    # Function to detect scams based on user input
def scam_detector():

    print("\n=============== SCAM DETECTOR REPORT ===============")
    print("                 CYBERGUARD - AI ")
    print("                  SCAM DETECTOR ")
    print("  ====================================================")

    message = input("Enter the message to analyze: \n").lower()

    score = 0

    scam_words = ["lottery", "prize", "winner", "urgent", 
                  "limited time", "click here", "free", 
                  "offer", "risk-free","guaranteed", "exclusive",
                    "act now", "money back", "no obligation", "instant access",
                 "special promotion","otp", "bank account", "password",
                 "social security number", "credit card", "personal information","urgent","click",
                 "verify", "update", "account", "login", "password reset",
                  "suspicious link", "malware", "phishing", "scam alert",
                  "fake website", "identity theft", "financial scam",
                  "investment opportunity", "get rich quick", "work from home",
                  "unclaimed funds", "inheritance", "charity scam",
                  "tech support scam", "prize claim", "lottery winner",
                  "urgent response required", "limited time offer",
                  "exclusive deal", "risk-free trial", "guaranteed results",
                  "act now to secure your spot"]

    print("\n Checking message...")
    detector = []

    for word in scam_words:
        if word in message:
            detector.append(word)
            score += 5

        if "https://" in message or "http://" in message:
            score += 5
        if "@" in message:
            score += 5
        print("Detected keywords:", detector)

        if len(detector) == 0:
            print("None")
        else:
             for item in detector:
                print("-", item)
        print()
    print("Threat Score:", score, "/100")

    if score >= 40:
            print("Verdict: HIGH RISK ")
    elif score >= 20:
            print("Verdict: SUSPICIOUS")
    else:
            print("Verdict: LOOKS SAFE")

    print("\n======================================")   

# menu for the user to select the desired functionality
while True:
    print("\nSelect an option:")
    print("=======================================")
    print("     1. Password Analyzer")
    print("     2. URL analyzer")
    print("     3. Email Analyzer")
    print("     4. Scam Detector")
    print("     5. Exit")
    print("=======================================")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        password = input("Enter Your Password :")
        password_analyzer(password)
    elif choice == '2':
        url_analyzer()
    elif choice == '3':
        email_analyzer()
    elif choice == '4':
        scam_detector()
    elif choice == '5':
        print("Thank you for using CyberGuard AI. Goodbye!")
        print("=======================================")
        break
    else:
        print("Invalid choice. Please try again.")

