def square():
    try:

            num = int(input("Enter a number"))
            while (num > 0):

                num = int(num)
                print(num*num)
    except:
        print("Enter a valid input")


square()