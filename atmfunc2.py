from atmfunction import ATM

if(__name__ == "__main__"):
    atm = ATM() 
    a = "Welcome To SBI Atm"
    print(a.center(120,"~"))
    print("________________________________________")
    user = input("Enter Username: ")
    user.lower()
    try:
        with open("atm.txt","r") as ap:
            for x in ap:
                x = x.split(",")
                if(user == x[0]):
                   pin = int(input("Enter Pin: "))
                   atm.PinChecker(pin,user)
                   break
    except:
         print("No user exist like" ,user,"...")