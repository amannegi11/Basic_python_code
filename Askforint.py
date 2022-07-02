def askint():
    '''the function i have created will try to convert user input into integer if possible'''
    while True:
        try:
            a=int(input("Enter the value"))
            print(f"{a} is an integer")
            break
        except Exception as e:
            print(" Looks like your input is " , e)
print(askint())
