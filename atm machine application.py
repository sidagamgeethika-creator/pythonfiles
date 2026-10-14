#ATM APPLICATION
pwd = 1234
acc=100000
while True:
    card=(input("insert the card"))
    if card == "c":
        print("welcome geethika")
        password=int(input("enter the password:"))
        if password ==pwd:
           option=int(input('''choose the option
                            1.balance enq
                            2.withdrawal'''))
           if option==1:
               print("aacc balnce is:",acc)
           elif option==2:
                   money=int(input("enter the money"))
                   print(money)
                   balance=acc-money
                   print("rem balance",balance)
           else:
               print("invalid option")
        else:
            print("invalid password")
    else:
        print("invalid card")
                      
                        
           
      
