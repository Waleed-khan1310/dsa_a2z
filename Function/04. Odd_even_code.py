#Now lets create a even odd program with function
def evenodd(x): 
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

evenodd(int(input("Enter your input to find even or odd: ")))