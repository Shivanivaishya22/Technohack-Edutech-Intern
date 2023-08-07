import random
import string

def PasswordGenrator():
    print("-----------Random Password Generator------------")
    l = string.ascii_lowercase  #for small letters
    u = string.ascii_uppercase   #for capital letters
    a = string.digits     #for numbers
    c = string.punctuation    #for special characters

    passlen = int(input("Enter Length of your password: "))
    combine = l+u+a+c
    pswd = "".join(random.sample(combine , passlen))
    print(f"Your Password is {pswd}")

PasswordGenrator()
