import random
g = "Rock Paper Scissors Game using Python"
print(g.center(120,"-"))
print("Type 0 for Rock,\n Type 1 for Paper,\n Type 2 for Scissor...")
user_choice = int(input("Enter Your Choice(0,1,2): "))
comp_choice = random.randint(0,2)
print(f"Computer'choice: {comp_choice}")

if(comp_choice > user_choice):
    print("Oopss!! You Loose....")
elif(comp_choice < user_choice):
    print("Congratulation , You Won!!!")
elif(comp_choice == user_choice):
    print("Its Draw...")
else:
    print("Please Enter Valid Response...")