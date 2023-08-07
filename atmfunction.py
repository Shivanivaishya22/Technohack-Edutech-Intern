class ATM:

    def PinChecker(self,pin,user):
        try:
            with open ("atm.txt", "r") as ap:
                for x in ap:
                    x = x.split(",")
                    if(pin == int(x[1]) and user==x[0]):
                        self.Welcome(user , pin)
                        break
        except:
            print("Invalid Credentials...")        

    def Welcome(self,user,pin):
        print('**************************')
        print('----------ATM SYSTEM-----------')
        print("Welcome" , user,",")
        response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nDeposite____(D)  \nQuit_______(Q) \n: ').lower()
        print('*******************************')
        print('-------------------------------')
        if(response == "s"):
            # print("hiii")
            self.Statement(user,pin)
        elif(response == "w"):
            self.Withdrawl(user, pin)
        elif(response == "d"):
            self.Deposite(user,pin)
        elif(response == "q"):
            self.Exit(user, pin)
        else:
            print("------RESPONSE NOT VALID------")


    def Statement(self,user,pin):
        print("hello")
        with open("atm.txt" , "r") as ap:
            for x in ap:
                x = x.split(",")
                if(user == x[0] and pin == int(x[1])):
                    print('---------------------------------------------')
                    print('*********************************************')
                    print(user , "You Have ",x[2],"Rupees In Your Account. ")
                    print('---------------------------------------------')
                    print('*********************************************')

    def Withdrawl(self,user , pin):
        found = False
        nlist = []
        with open("atm.txt" , "r") as ap:
            for x in ap:
                x = x.split(",")
                if(user == x[0] and pin == int(x[1])):
                    cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
                    c = int(x[2])
                    if(cash_out > int(x[2])):
                        print('-----------------------------')
                        print('YOU HAVE INSUFFICIENT BALANCE.')
                        print('-----------------------------')           
                    elif(cash_out <= c ):
                        c = c - cash_out
                        print('YOUR NEW BALANCE IS: ', c , 'RUPEES.')
                        (x[2]) = str(c)
                        found = True
                nlist.append(x)
                print(nlist)  
        
        if (found == True):
                with open("atm.txt", "w") as fp:
                    for y in nlist:
                       y = ",".join(y)
                       fp.write(y)
                       fp.write("\n")

    def Deposite(self,user,pin):
        
            found = False
            nlist = []
            with open("atm.txt" , "r") as ap:
                for x in ap:
                    x = x.split(",")
                    if(user == x[0] and pin == int(x[1])):
                        cash_in = int(input('ENTER AMOUNT YOU WOULD LIKE TO LODGE: '))
                        c = int(x[2])
                        if(cash_in < 100):
                            print('-----------------------------')
                            print('AMOUNT YOU WANT TO LODGE MUST BE ATLEAST 100 RUPEES')
                            print('-----------------------------')
                        elif(cash_in <= c):
                            c = c + cash_in
                            print('YOUR NEW BALANCE IS: ', c , 'RUPEES.')
                            
                            (x[2]) = str(c)
                            found = True
                    nlist.append(x)
                print(nlist)   
        
            if (found == True):
                with open("atm.txt", "w") as fp:
                    for y in nlist:
                       y = ",".join(y)
                       fp.write(y)
                       fp.write("\n")
    
    def Exit(self):
        exit()