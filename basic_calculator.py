def cal(num1,num2,operation):
    
        if operation=="+":
            return num1+num2
        elif operation=="-":
            return num1-num2
        elif operation=="*":
            return num1*num2
        elif operation=="/":
            try:
                return num1/num2
            except ZeroDivisionError:
                return "Your process has Zero Division Error"
        else:
            return "your operation is not valid"
while True:
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the second number: "))
        operation=input("Choose your operation(+,-,*,/):")
        print(cal(num1,num2,operation))
        z=input("Devam etmek ister misiniz?(Yes,No)")
        if z.lower()=="no":
            break
