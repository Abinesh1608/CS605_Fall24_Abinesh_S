
print("\nWelcome to Simple Calculator!\n")

def UserInput(entry):
    while True:
        try:
            return float(input(entry))
        except ValueError:
            print("\nInvalid input. Please enter a valid number.\n")
            Calculator()
            

def Calculator():
    
    num1 = UserInput(("Enter the First Number: "))
    num2 = UserInput(("Enter the Second Number: "))
    
    def Operation(num1,num2):
        print("\nSelect an Operation: \n\n 1. Addition \n 2. Subtraction \n 3. MUltiplication \n 4. Division \n")
        cal_type = UserInput(("Enter the operation number: "))
        if cal_type == 1:
            print(f"{num1} + {num2} = {num1+num2}")
        elif cal_type == 2:
            print(f"{num1} - {num2} = {num1-num2}")
        elif cal_type == 3:
            print(f"{num1} * {num2} = {num1*num2}")
        elif cal_type == 4:
           
            try:
                print(f"{num1} / {num2} = {num1 / num2}")
            except ZeroDivisionError:
                print( "\n Error! Division by zero is not allowed.")
        else :
            print("Input Invalid ! Enter a valid Number between 1-4 !")
        
        Another_cal()
            
    Operation(num1,num2)

def Another_cal():
        cal = input("\nDo you want to perform another calculation? (yes/no): ")

        if cal == "yes":
            Calculator()
        elif cal == "no":
            print("\n Have a nice day!\n")
        else :
            print("\nInvalid ! Enter a Valid Argument !!")
            Another_cal()

Calculator() 
    
