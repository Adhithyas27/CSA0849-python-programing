#Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a
#list [odd,even], where odd is the sum of squares of all the odd numbers in l and even is the
#sum of squares of all the even numbers in l.

a=int(input("Enter the total numbers:"))
odd=0
even=0
for i in range(a):
    b=int(input("Enter the number:"))
    if(b%2==0):
          even+=b
    else:odd+=b
print("sum of odd and even",[odd,even])
print("Sum of square of odds and even",[odd**2,even**2])
    
