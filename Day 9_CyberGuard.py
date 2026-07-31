# Day - 9
# Topic : CyberDuard
# Project : CyberGuard AI

print("=======================================")
print("          CyberGuard AI           ")
print("=======================================")

from datetime import datetime

# Function to analyze password strength
password_result = "Not Checked"
password_score = 0

password_done = False

def password_analyzer(password):
    global password_result
    global password_score
    global password_done

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
    password_done = True

# Function to scan URL and check its validity and domain reputation

url_result = "Not Checked"
url_score = 0
url_done = False
def url_analyzer():
     
     global url_result
     global url_score
     global url_done
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
     url_done = True


email_result = "Not Checked"
email_score = 0
email_done = False

def email_analyzer():
      global email_result
      global email_score
      global email_done

      email = input("Enter the email address to analyze: ")
      print("\n=============== EMAIL ANALYZER REPORT ===============")
    
   
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
      risk_score = 0

      if domain in personal_domains:
        risk_score += 50
      if len(username) < 3:
        risk_score += 20
        
      print("Security score :", risk_score, "/100")

      if "@" in email and "." in email:
        email_result = "VALID"
        email_score = 25
      else:
        email_result = "INVALID"
        email_score = 0
        
      email_done = True

      input("\n press enter to return to main menu ...")

    # Function to detect scams based on user input

scam_result = "Not Checked"
scam_score = 0
scam_done = False

def scam_detector():

    global scam_result
    global scam_score
    global scam_done

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
 
    if len(reasons) == 0:
        print("No suspicious reasons found.")
    else:
        for reason in reasons:
            print("-", reason)
    print("\n==============================================")   
    scam_done = True

def security_report():
     current_time = datetime.now()
     score = 0

     print("\n")
     print("="*55)
     print("        CYBERGUARD-AI SECURITY REPORT       ")
     print("="*55)

     date = current_time.strftime("%d-%m-%Y")
     time = current_time.strftime("%I:%M:%S %p")

     print("\nDATE    :",date) 
     print("TIME    :",time)

     
     print(f"\npasssword analysis:{password_result}")
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
        print("security level : CRITICAL ")
           

     print("-"*55)
     print("Over all security score:",total_score,"/100")
     print("Security level         :",level)
     print("-"*55)

    # scan summary 
     print("\n=========== SCAN SUMMARY ========")

     print(password_result)
     print(url_result)
     print(email_result)
     print(scam_result)

     completed = 0

     if password_done:
        completed += 1
     if url_done:
        completed += 1
     if email_done:
        completed += 1
     if scam_done:
        completed += 1

     print(f"\n Completed scans :{completed}/4")

     if completed == 4:
         print("Status : Full security scan completed")
     elif completed >=2:
         print("Status : Partical security scan")
     else:
         print("Status : Scan more modules")

    # create AI Security recommendations 
     print("\n======== AI SECURITY RECOMMENDATIONS ======== ")

     if completed != 4:
         print("\n- Run all modules for accurate security analysis...!")

     # AI Recommendations

     if password_result == "WEAK":
        print("- Improve your password strength.")
        print("- Use a password with at least 8 characters.")
        print("- Include uppercase, lowercase, numbers and symbols.")
        
     elif password_result == "MEDIUM":
        print("- Add more special characters to strengthen your password.")

     else:
        print("- Password security is good.")

     print()

     if url_result == "HIGH RISK":
        print("- Do not open suspicious websites.")
     elif url_result == "SAFE":
        print("- URL looks safe.")
     else:
        print("- URL analysis has not been performed.")

     print()

     if email_result == "SUSPICIOUS":
        print("- Verify the sender before clicking links.")
     elif email_result == "SAFE":
        print("- Email appears safe.")
     else:
        print("- Email analysis has not been performed.")

     print()

     if scam_result == "SCAM":
        print("- Possible scam detected. Avoid sharing OTP or bank details.")
     elif scam_result == "SAFE":
        print("- No scam indicators detected.")
     else:
        print("- Scam detector has not been used.")

     print("\n============= FINAL AI VERDICT =============")

     if total_score >= 90:
        print("\nYour device appears to be highly secure.")

     elif total_score >= 70:
        print("Your device is secure, but minor improvements are recommended.")

     elif total_score >= 50:
        print("Your device has moderate security risks.")

     else:
        print("Warning! Your device may be vulnerable to cyber threats.")

     if completed == 4:
        print("\nAll security modules have been analyzed successfully.")

     else:
        print(f"Only {completed}/4 modules were analyzed.")
        print("Run the remaining modules for a complete security report.")

     print("\n" + "=" * 60)
     print("        Thank you for using CyberGuard AI")
     print("             Stay Safe. Stay Secure.")
     print("=" * 60)


# create export report 
def export_report():
    global password_result
    global url_result
    global email_result
    global scam_result

    global password_score
    global url_score
    global email_score
    global scam_score

    if (password_result == "Not Checked" and url_result == "Not Checked"
    and email_result == "Not Checked" and scam_result == "Not Checked"):

        print("\n - No analysis found.")
        print(" - Please run at least one analyzer before exporting the report.")
        return

    total_score = password_score + url_score + email_score + scam_score

    from datetime import datetime

    current_time = datetime.now()

    date = current_time.strftime("%d-%m-%Y")
    time = current_time.strftime("%I:%M:%S %p")

    file = open("CyberGuard_Report.txt", "a")

    file.write("\n"+"="*40 + "\n")
    file.write("CYBERGUARD AI SECURITY REPORT\n")
    file.write("="*40 + "\n")

    file.write(f"Date : {date}\n")
    file.write(f"Time : {time}\n\n")

    file.write(f"Password Analysis : {password_result}\n")
    file.write(f"URL Analysis      : {url_result}\n")
    file.write(f"Email Analysis    : {email_result}\n")
    file.write(f"Scam Detector     : {scam_result}\n\n")
    file.write(f"Overall Score : {total_score}/100\n")

    if total_score >= 90:
        level = "EXCELLENT"
    elif total_score >= 70:
        level = "GOOD"
    elif total_score >= 50:
        level = "AVERAGE"
    else:
        level = "POOR"

    file.write(f"Security Level : {level}\n")

    file.write("\n"and"=" * 55 + "\n")
    file.write("        AI SECURITY RECOMMENDATIONS\n")
    file.write("=" * 55 + "\n\n")

    # password recommendation
    if password_result == "WEAK":
        file.write("- Use a stronger password.\n")
        file.write("- Include uppercase, lowercase, numbers and symbols.\n\n")

    elif password_result == "MEDIUM":
        file.write("- Add special characters for better security.\n\n")

    else:
        file.write("- Password strength is good.\n\n")

    # url recommendation
    if url_result == "HIGH RISK":
        file.write("- Avoid suspicious websites.\n\n")

    elif url_result == "SAFE":
        file.write("- URL appears safe.\n\n")

    # email recommendation
    if email_result == "SUSPICIOUS":
        file.write("- Verify sender before opening attachments.\n\n")

    elif email_result == "SAFE":
        file.write("- Email appears safe.\n\n")

    # scam recommendation
    if scam_result == "SCAM":
        file.write("- Never share OTP, passwords or banking details.\n\n")

    elif scam_result == "SAFE":
        file.write("- No scam indicators detected.\n\n")

    file.write("=" * 40 + "\n")
    file.write("        FINAL AI VERDICT\n")
    file.write("=" * 40 + "\n")

    if total_score >= 90:
        file.write("---Your device appears highly secure---\n")

    elif total_score >= 70:
        file.write("---Your device is secure with minor improvements recommended---\n")

    elif total_score >= 50:
        file.write("---Your device has moderate security risks---\n")

    else:
        file.write("---Warning! Your device may be vulnerable to cyber threats---\n")
    file.write("=" * 60 + "\n\n")

    file.close()
    print("\n"+"="*55)
    print("         Report Exported Successfully!")
    print("         File : CyberGuard_Report.txt")
    print("="*55)

def dashboard ():

    print("\n")
    print("=" * 50)
    print("        CYBERGUARD AI DASHBOARD")
    print("=" * 50)

    def status_icon(status):
     if status in ["STRONG", "SAFE", "VALID", "LOW RISK"]:
        return "✅"
     elif status == "Not Checked":
        return "⚪"
     else:
        return "⚠️"

    print(f"Password Status : {status_icon(password_result)} {password_result}")
    print(f"URL Status      : {status_icon(url_result)} {url_result}")
    print(f"Email Status    : {status_icon(email_result)} {email_result}")
    print(f"Scam Status     : {status_icon(scam_result)} {scam_result}")

    print("-" * 50)

    total_score = password_score + url_score + email_score + scam_score

    if total_score >= 90:
        level = "EXCELLENT"
    elif total_score >= 70:
        level = "GOOD"
    elif total_score >= 50:
        level = "AVERAGE"
    else:
        level = "POOR"

    print(f"Overall Score   : {total_score}/100")
    print(f"Security Level  : {level}")
    print("-"*50)

    from datetime import datetime

    current_time = datetime.now()

    completed = 0

    if password_result != "Not Checked":
        completed += 1
    if url_result != "Not Checked":
        completed += 1
    if email_result != "Not Checked":
        completed += 1
    if scam_result != "Not Checked":
        completed += 1

    print(f"Completed Scans : {completed}/4")
    print(f"Last Scan       : {current_time.strftime('%d-%m-%Y %I:%M %p')}")
    print("-"*50)

# menu for the user to select the desired functionality
while True:
    print("\nSelect an option:")
    print("="*50)
    print("     1. Password Analyzer")
    print("     2. URL analyzer")
    print("     3. Email Analyzer")
    print("     4. Scam Detector")
    print("     5. Security report")
    print("     6. Dashboard")
    print("     7. Export report")
    print("     8. Exit")
    print("===============================================")
    choice = input("Enter your choice (1-8): ")

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
        dashboard() 
    elif choice == '7':
        export_report()
    elif choice == '8':
        print("Thank you for using CyberGuard AI. Goodbye!")
        print("===========================================")
        break
    else:
        print("Invalid choice. Please try again.")
