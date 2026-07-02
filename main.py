from cipher import encoder, decoder

running = True
while running:
    print("======================")
    #print()
    print("SECRET CIPHER")
    #print()
    print("======================")

    print("1. Encrypt a message.")
    print("2. Decrypt a message.")
    print("3. Exit.")
    
    choice = input("Choose one of the three options above: ")
  
    if choice == "1":
        message = input("Enter your message:")
        try:
            key = int(input("Enter your key! It can be any interger except zero: "))  
            encrypted = encoder(message, key)
            print("\nEncrypted message:")
            print(encrypted)
            print()
        except ValueError:
            print("Invalid key! Returning to the main menu.")
            print() 

    elif choice == "2":
        message = input("Enter your message: ")
        try:
            key = int(input("Enter your key! It can be any interger except zero: "))
            decrypted = decoder(message, key)
            print("\nDecrypted message:")
            print(decrypted)
            print()
        except ValueError:
            print("Invalid key! Returning to the main menu.")
            print()
       

    elif choice == "3":
        print("\nThank you for using Secret Cipher!")
        running = False

    else:
        print("Invalid choice.\nPlease try again.")
       
