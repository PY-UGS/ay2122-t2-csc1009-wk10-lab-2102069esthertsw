# prompt user for max and min integers
max = int(input("Enter your maximum integer: "))
min = int(input("Enter your minimum integer: "))

x = max
while(x>=min):
#     print values from max to min, decrement by 2
    print("value of x: " , x )
    x-=2
