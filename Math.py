lower=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
num=int(input("Enter number to be divided with:"))

for i in range(lower, upper+1):
    if(i%num == 0):
        print(i)