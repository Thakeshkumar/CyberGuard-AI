# Day - 9
# Topic : CyberDuard
# Project : CyberGuard AI

print("=======================================")
print("          CyberGuard AI           ")
print("=======================================")


# Function to analyze password strength
password_result = "Not Checked"
def password_analyzer(password):
    global password_result
    global password_score

    score = 0

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
        password_result = "STRONG"
        password_score = 25

    elif len(password) >= 8:
        print("password strength : MEDIUM")
        password_result = "MEDIUM"
        password_score = 15

    else: 
        print("password strength : WEAK")
        password_result = "WEAK"
        password_result = 5

        print("Password must be atleast 8 characters long")
    
    if password_result == "STRONG":
     score += 25
    elif password_result == "MEDIUM":
     score += 15

    if upper == 0:
            print("Add atleast 1 uppercase letter")

    if lower == 0:
            print("Add atleast 1 lowercase letter")

    if number == 0:
            print("Add atleast 1 number")

    if special == 0:
            print("Add atleast 1 special character")

    if password_result == "WEAK":
        print("- Use at least 8 characters.")
        print("- Include uppercase, lowercase, numbers and special characters.")

    elif password_result == "MEDIUM":
        print("- Add more special characters.")
        print("- Increase password complexity.")

    else:
        print("- Password is secure.")

# Function to scan URL and check its validity and domain reputation

url_result = "Not Checked"
def url_analyzer():
     
     global url_result
     global url_score
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
            url_result = "SAFE"
            url_score = 25

     elif score <= 50:
            print("Verdict      : MEDIUM RISK")
            url_result = "SUSPICIOUS"
            url_score = 15

     else:  
            print("Verdict      : HIGH RISK")
            url_result = "DANGEROUS"
            url_score = 5

     if url_result == "SAFE":
      score += 25
     
     if ".com" in url:
          print("🌍 Commercial Website (.com) Generally Safe" )

     elif ".org" in url:
          print("🏢 Organization Website (.org) Generally Safe" )

     elif ".net" in url:
          print("🌐 Network Website (.net) Generally Safe")

     else:
          print("Unknown Domain")

     if url_result != "SAFE":
         print("- Avoid opening suspicious websites.")
         print("- Always verify HTTPS and domain name.")

     else:
        print("- URL looks safe.")
        input("\n  Press Enter To Return To Main Menu ...")

email_result = "Not Checked"
def email_analyzer():
      global email_result
      global email_score

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

      if email_result == "SAFE":
       score += 25
       email_score = 25
      else:
          email_score = 5

    #Adding risk score based on email type
      score= 0

      if domain in personal_domains:
        score -= 50

      if len (username) < 3:
        score -= 20

      print("Security score:",score ,"/100")

      if email_result != "SAFE":
        print("- Verify sender email before replying.")
        print("- Do not open unknown attachments.")

      else:
        print("- Email appears safe.")

        input("\n press enter to return to main menu ...")

    # Function to detect scams based on user input

scam_result = "Not Checked"
def scam_detector():

    global scam_result
    global scam_score

    print("\n=============== SCAM DETECTOR REPORT ===============")
    print("----           CYBERGUARD - AI       ----")
    print("     ----       SCAM DETECTOR      ----    ")
    print("="*55)

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

    reasons = []

    for word in scam_words  :
        if word in message.lower():
            print("Keyword Found :", word)
            score += 10
            reasons.append(f"Suspicious keyword detected : {word}")

        if "https://" in message or "http://" in message:
            score += 10
        if "@" in message:
            score += 10
        if "!" in message:
            score += 10

    print("\n======================================")
    print("     SCAM DETECTOR REPORT        ")
    print("========================================")

    print("Threat Score:", score, "/100")

    if score <= 20:
        print("RISK LEVEL: LOW RISK")
        print("Status    : Message lools mostely safe")
        scam_result = "LOW RISK"
        scam_score = 25

    elif score <= 50:
        print("RISK LEVEL: MEDIUM RISK")
        print("Status    : Be careful before taking action")
        scam_result = "MEDIUM RISK"
        scam_score = 15

    else:
        print("RISK LEVEL: HIGH RISK")
        print("Status    : Possible scam message")
        scam_result = "HIGH RISK"
        scam_score = 5
    
    # key detection 
    if word == "otp":
        reasons.append("OTP request detected")
    elif word == "verify":
        reasons.append("Verification request found")
    elif word == "click":
        reasons.append("Suspicious click instruction")
    elif word == "account":
        reasons.append("Account related message")
    elif word == "bank":
        reasons.append("Bank related content")

    print("\n reasons :")
 
    if scam_result == "SAFE":
     score += 25

    if scam_result != "SAFE":
        print("- Do not click unknown links.")
        print("- Never share OTP or passwords.")
        print("- Verify messages from official sources.")

    else:
        print("- No scam indicators detected.")

    if len(reasons) == 0:
        print("No suspicious reasons found.")
    else:
        for reason in reasons:
            print("-", reason)
    print("\n==============================================")   

def security_report():
     score = 0

     print("\n")
     print("="*55)
     print("        CYBERGUARD-AI SECURITY REPORT       ")
     print("="*55)

     
     print(f"passsword analysis:{password_result}")
     print(f"URl analysis      :{url_result}")
     print(f"Email analysis    :{email_result}")
     print(f"scam detector     :{scam_result}")

     print("="*55)

     total_score = (password_score + url_score + email_score + scam_score)

     if total_score >= 90:
         level = "EXCELLENT"
     elif total_score >= 70:
          level = "GOOD"
     elif total_score >= 50:
          level = "AVERAGE"
     else:
          level = "POOR"
 
     if scam_result == "SAFE":
      score += 25

     if score >= 80:
        print("Security Level : EXCELLENT")

     elif score >= 60:
        print("Security Level : GOOD")

     elif score >= 40:
        print("Security Level : AVERAGE")

     else:
         print("Security Level : DANGER")

     print("-"*55)
     print("Over all security score:",total_score,"/100")
     print("Security level         :",level)
     print("-"*55)

     print("\n==============================")
     print("   AI SECURITY RECOMMENDATIONS ")
     print("================================")

# menu for the user to select the desired functionality
while True:
    print("\nSelect an option:")
    print("="*50)
    print("     1. Password Analyzer")
    print("     2. URL analyzer")
    print("     3. Email Analyzer")
    print("     4. Scam Detector")
    print("     5.Security report")
    print("     6. Exit")
    print("===============================================")
    choice = input("Enter your choice (1-6): ")

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
        security_report() 
    elif choice == '6':
        print("Thank you for using CyberGuard AI. Goodbye!")
        print("===========================================")
        break
    else:
        print("Invalid choice. Please try again.")

