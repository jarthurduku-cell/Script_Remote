username = input("Enter username:")
password = input(" Enter password: ")

attempts = 3
count = 1

while attempts > 0:
    
    if len(password) < 8:
        print("\nPassword validation failed:")
        print("- Too short (minimum 8 characters)")
        
        if not any(char.isupper() for char in password):
            print("- Missing uppercase letter")
        
        if not any(char.islower() for char in password):
            print("- Missing lowercase letter")

        if not any(char.isdigit() for char in password):
            print("- Missing digit")
            
        if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
            print("- Missing special character")
        
        if username in password:
            print("- Contains username")
        
        if "password" in password.lower():
            print("- Contains forbidden word: password")
    
        print()
            
        attempts -= 1 
        if attempts > 0:    
          print(f"Attempts remaining: {attempts}")
          password = input("\nEnter password: ")
          count += 1 
        else:
         print("Account locked. Maximum attempts exceeded.")
        
    if len(password) >= 8:
    
        if any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password) and not username in password and not "password" in password.lower():
            print("\nPassword accepted.")

            print("\nSecurity Report:")
            print("Attempts used:",count)
            print("Username:",username)

            print("\nPassword strength:")
            passwordLength = len(password) - 8
            digitList = [int(c) for c in password if c.isdigit()]
            numDigits = len(digitList)

            specialCharacters = [char in  "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password]

            all_true = []
            for item in specialCharacters:
                if item is True:
                  all_true.append(item)

            numSpecial = 2 * len(all_true)

            print("Length bonus:", passwordLength,"points")
            print("Digit bonus:", numDigits,"points")
            print("Special character bonus:", numSpecial,"points")
            total = passwordLength + numDigits + numSpecial
            
            twelveBonus = 1
            sixteenBonus = 1

            if len(password) >= 12 and len(password) < 16:   
                print("12+ characters bonus:", twelveBonus,"point")
                total = passwordLength + numDigits + numSpecial + twelveBonus
                print("Total:", total,"points") 
             
            elif len(password) >= 12 and len(password) >= 16: 
                print("12+ characters bonus:", twelveBonus,"point")
                print("16+ characters bonus:", sixteenBonus,"point")
                total = passwordLength + numDigits + numSpecial + twelveBonus + sixteenBonus
                print("Total:", total,"points")
            else:
                print("Total:", total,"points")

            if total >= 0 and total <= 5:
                print("Rating: Weak")
            elif total >= 6 and total <= 10:
                print("Rating: Medium")
            else:
                print("Rating: Strong")
            
            print("\nAccess granted.")
            
            break
        else:
            print("\nPassword validation failed:")

        if not any(char.isupper() for char in password):
            print("- Missing uppercase letter")

        if not any(char.islower() for char in password):
            print("- Missing lowercase letter")
        
        if not any(char.isdigit() for char in password):
            print("- Missing digit")
            
        if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
            print("- Missing special character")
        
        if username in password:
            print("- Contains username")
            
        if "password" in password.lower():
            print("- Contains forbidden word: password")
        
        print()
        attempts -= 1  
        if attempts > 0:    
          print(f"Attempts remaining: {attempts}")
          password = input("\nEnter password: ")
          count += 1 
        else:
          print("Account locked. Maximum attempts exceeded.")

        
        

        
